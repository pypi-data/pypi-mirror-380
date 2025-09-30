import os
import logging
import random
from pathlib import Path
from functools import reduce, partial
from operator import getitem
from datetime import datetime
from .utils.util import read_yaml, write_yaml

def setup_logging(save_dir, log_config='logger/logger_config.json', default_level=logging.INFO):
    """
    Setup logging configuration
    """
    log_config = Path(log_config)
    if log_config.is_file():
        config = read_yaml(log_config)
        # modify logging paths based on run config
        for _, handler in config['handlers'].items():
            if 'filename' in handler:
                handler['filename'] = str(save_dir / handler['filename'])

        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)

class ConfigParser:
    def __init__(self, config, resume=None, modification=None, run_id=None):
        """
        class to parse configuration yaml file. Handles hyperparameters for training, initializations of modules, checkpoint saving
        and logging module.
        :param config: Dict containing configurations, hyperparameters for training. contents of `config.yaml` file for example.
        :param resume: String, path to the checkpoint being loaded.
        :param modification: Dict keychain:value, specifying position values to be replaced from config dict.
        :param run_id: Unique Identifier for training processes. Used to save checkpoints and training log. Timestamp is being used as default
        """
        # load config file and apply modification
        self._config = _update_config(config, modification)
        self.resume = resume

        # random seed
        if 'train_seed_list' not in self._config or self._config['train_seed_list'] is None:
            self._config['train_seed_list'] = random.sample(range(1, 10000), 5)

        # set save_dir where trained model and log will be saved.
        save_dir = Path(self.config['trainer']['save_dir'])

        exper_name = self.config['name']
        if run_id is None: # use timestamp as default run-id
            run_id = datetime.now().strftime(r'%m%d_%H%M%S')
        self._save_dir = save_dir / 'models' / exper_name / run_id
        self._log_dir = save_dir / 'log' / exper_name / run_id

        # make directory for saving checkpoints and log.
        exist_ok = run_id == ''
        self.save_dir.mkdir(parents=True, exist_ok=exist_ok)
        self.log_dir.mkdir(parents=True, exist_ok=exist_ok)

        # save updated config file to the checkpoint dir
        write_yaml(self.config, self.save_dir / 'config.yaml')

        # configure logging module
        setup_logging(self.log_dir)
        self.log_levels = {
            0: logging.WARNING,
            1: logging.INFO,
            2: logging.DEBUG
        }
    @classmethod
    def from_args(cls, args, options='', arg_list=None):
        """
        Initialize this class from some CLI arguments. Used in train, test.
        :param args: ArgumentParser object.
        :param options: Custom options to add.
        :param arg_list: List of arguments to simulate command-line input.
        """
        if arg_list is not None:
            args = args.parse_args(arg_list)
        else:
            for opt in options:
                args.add_argument(*opt.flags, default=None, type=opt.type)
            if not isinstance(args, tuple):
                args = args.parse_args()

        # if args.device is not None:
        #     os.environ["CUDA_VISIBLE_DEVICES"] = args.device

        if args.resume is not None:
            resume = Path(args.resume)
            cfg_fname = resume.parent / 'config.yaml'
        else:
            assert args.config is not None, "Configuration file needs to be specified. Add '-c config.yaml', for example."
            resume = None
            cfg_fname = Path(args.config)

        config = read_yaml(cfg_fname)
        
        # inherit base config
        if '_base_' in config:
            base_config_path = Path(cfg_fname).parent / config['_base_']
            base_config = read_yaml(base_config_path)
            # deep merge config
            config = _deep_merge(base_config, config)
            del config['_base_']  # remove inherit mark

        if args.config and resume:
            config.update(read_yaml(args.config))

        modification = {opt.target: getattr(args, _get_opt_name(opt.flags)) for opt in options}
        return cls(config, resume, modification)    

    def init_obj(self, name, module, *args, **kwargs):
        """
        Finds a function handle with the name given as 'type' in config, and returns the
        instance initialized with corresponding arguments given.

        This function will support both initializing models (that expect a dictionary of arguments)
        and optimizers (which expect trainable parameters as the first argument).
        """
        module_name = self[name]['type']
        module_args = dict(self[name]['args'])
        
        # Ensure no overwriting in kwargs
        assert all([k not in module_args for k in kwargs]), 'Overwriting kwargs given in config file is not allowed'
        module_args.update(kwargs)

        # Check if we have *args, use them as the first parameters (e.g., for optimizers)
        if args:
            return getattr(module, module_name)(*args, **module_args)
        
        # Otherwise, treat as model or similar initialization with just keyword arguments
        return getattr(module, module_name)(**module_args)


    def init_ftn(self, name, module, *args, **kwargs):
        """
        Finds a function handle with the name given as 'type' in config, and returns the
        function with given arguments fixed with functools.partial.

        `function = config.init_ftn('name', module, a, b=1)`
        is equivalent to
        `function = lambda *args, **kwargs: module.name(a, *args, b=1, **kwargs)`."
        """
        module_name = self[name]['type']
        module_args = dict(self[name]['args'])
        assert all([k not in module_args for k in kwargs]), 'Overwriting kwargs given in config file is not allowed'
        module_args.update(kwargs)
        return partial(getattr(module, module_name), *args, **module_args)

    def __getitem__(self, name):
        """Access items like ordinary dict."""
        return self.config[name]

    def get_logger(self, name, verbosity=2):
        msg_verbosity = 'verbosity option {} is invalid. Valid options are {}.'.format(verbosity, self.log_levels.keys())
        assert verbosity in self.log_levels, msg_verbosity
        logger = logging.getLogger(name)
        logger.setLevel(self.log_levels[verbosity])
        return logger
    
    def get(self, key, default=None):
        return self._config.get(key, default)
    
    def __setitem__(self, key, value):
        self._config[key] = value
    # setting read-only attributes
    @property
    def config(self):
        return self._config

    @property
    def save_dir(self):
        return self._save_dir

    @property
    def log_dir(self):
        return self._log_dir

# helper functions to update config dict with custom cli options
def _update_config(config, modification):
    if modification is None:
        return config

    for k, v in modification.items():
        if v is not None:
            _set_by_path(config, k, v)
    return config

def _deep_merge(base_dict, override_dict):
    """deep merge two dicts"""
    result = base_dict.copy()
    for key, value in override_dict.items():
        if key in result and isinstance(result[key], dict) and isinstance(value, dict):
            result[key] = _deep_merge(result[key], value)
        else:
            result[key] = value
    return result

def _get_opt_name(flags):
    for flg in flags:
        if flg.startswith('--'):
            return flg.replace('--', '')
    return flags[0].replace('--', '')

def _set_by_path(tree, keys, value):
    """Set a value in a nested object in tree by sequence of keys."""
    keys = keys.split(';')
    _get_by_path(tree, keys[:-1])[keys[-1]] = value

def _get_by_path(tree, keys):
    """Access a nested object in tree by sequence of keys."""
    return reduce(getitem, keys, tree)

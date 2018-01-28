# coding: utf-8

# Standard Libraries
import json
import logging
from pathlib import Path
from pathlib import PosixPath

# Cfgtree modules
from cfgtree.storages._single_file import SingleFileStorage

log = logging.getLogger(__name__)


class JsonFileConfigStorage(SingleFileStorage):
    """
    Settings are stored in a single JSON file

    Example:

    .. code-block:: javascript

        {
            'version': 1,
            'general': {
                'verbose': true ,
                'logfile': 'logfile.log'
            }
        }

    Usage:

    .. code-block:: python

        class MyAppConfig(ConfigBaseModel):

            environ_var_prefix = "MYAPP_"

            storage = JsonFileConfigStorage(
                environ_var="MYAPP_COMMON_CONFIG_FILE",
                long_param="--config",
                short_param="-c",
                default_filename="config.json",
            )

            cmd_line_parser = # ...

            model = {
                # repeat in model so the arguments in described in --help
                "configfile": ConfigFileCfg(long_param="--config-file", summary="Config file"),
                # ...
            }

    """

    json_configstorage_default_filename = None
    """Default filename for the configuration file

    Example::

        myconfig.json
    """

    json_configstorage_environ_var = None
    """Environment variable to set the configuration file name

    Example::

       DOPPLERR_COMMON_CONFIG_FILE="myconfig.json"
    """

    json_configstorage_short_param = None
    """Short parameter to specify the configure file name

    Example::

        -g myconfig.json
    """

    json_configstorage_long_param = None
    """Short parameter to specify the configure file name

    Example::

        --config-file myconfig.json
    """

    def load_bare_config(self, config_file_path: Path):
        with config_file_path.open() as f:
            return json.load(f)

    def save_bare_config_dict(self, bare_cfg):
        with PosixPath(self.__resolved_config_file).open('w') as f:
            f.write(json.dumps(bare_cfg, sort_keys=True, indent=4, separators=(',', ': ')))

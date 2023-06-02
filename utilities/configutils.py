from configparser import ConfigParser
from base_settings import APPLICATION_PATH
import os

CONFIG_FILE = os.path.join(APPLICATION_PATH, 'config.ini')


def get_config(instance: str) -> dict:
    """
    Retrieve configuration from config.ini convert to dictionary for TM1PY
    :param instance: Config section name
    :return: dict of entries for TM1PY
    """
    config = ConfigParser()
    config.read(CONFIG_FILE)
    _cloud = str_to_bool(config[instance]['cloud'])
    if _cloud:
        _config = {
            'base_url': config[instance]['address'],
            'namespace': 'LDAP',
            'verify': True,
            'async_requests_mode': True
        }
    else:
        _config = {
            'address': config[instance]['address'],
            'port': config[instance]['port'],
            'ssl': config[instance]['ssl'],
            'namespace': config[instance]['namespace'],
            'gateway': config[instance]['gateway']
        }
    return _config


def save_config(instance: str, config: dict) -> None:
    """
    Create/Update section in Config.ini
    :param instance: string of section name
    :param config: dict to be saved
    :return:
    """
    conf = ConfigParser()
    conf.read(CONFIG_FILE)
    conf[instance] = config
    conf.write(open(CONFIG_FILE, 'w'))


def retrieve_sections() -> list:
    """
    Retrieve list of sections within config.ini
    :return: list of sections
    """
    _sections = ['']
    config = ConfigParser()
    config.read(CONFIG_FILE)
    for section in config.sections():
        _sections.append(section)
    return _sections


def retrieve_section_for_update(instance: str) -> dict:
    """
    Used to populate "update_window"
    :param instance: string of section to retrieve
    :return: dict of entries within section
    """
    config = ConfigParser()
    config.read(CONFIG_FILE)
    return dict(config.items(instance))


def str_to_bool(string: str) -> bool:
    """
    Convert string to boolean
    :param string: string representation of answer
    :return: bool
    """
    return string.lower() in ['y', 'yes', 't', 'true', 'on', '1']

import os
from configparser import ConfigParser, ExtendedInterpolation


def set_certificate():
    PTB_CERT_PATH = os.path.join(os.path.dirname(__file__), './petrobras-ca-root.pem')
    os.environ['REQUESTS_CA_BUNDLE'] = PTB_CERT_PATH


def load_config(config_name):
    config = ConfigParser(interpolation=ExtendedInterpolation())
    config.read(os.path.join(os.path.dirname(__file__), config_name), 'UTF-8')
    return config


def configure_env(config_name):
    set_certificate()
    return load_config(config_name)



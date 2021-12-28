import configparser


def parse_config():
    config = configparser.RawConfigParser()
    config.read('./CONFIG.ini')
    return config

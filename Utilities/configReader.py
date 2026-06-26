import os
from configparser import ConfigParser

# Resolve conf.ini relative to the project root so `behave` works no matter
# which directory it is launched from (more robust than a hard-coded ".\" path).
CONFIG_PATH = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "ConfigurationData",
    "conf.ini",
)


def readConfig(section, key):
    config = ConfigParser(interpolation=None)
    config.read(CONFIG_PATH, encoding="utf-8")
    return config.get(section, key)

from typing import Dict


import json

class ConfigParser(object):
    _instance = None

    config: Dict = None

    def __init__(self):
        with open('.config.json') as json_file:
            self.config = json.load(json_file)

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(ConfigParser, cls).__new__(
                                cls, *args, **kwargs)
        return cls._instance

    def get(self, key):
        return self.config[key]
    
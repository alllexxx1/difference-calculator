import json
import yaml
from yaml.loader import BaseLoader


def deserialize_format(file):
    if file.endswith('.yaml') or file.endswith('.yml'):
        with open(file) as file:
            return yaml.load(file, Loader=BaseLoader)
    elif file.endswith('.json'):
        with open(file) as file:
            return json.load(file)
    else:
        raise Exception('Invalid format')

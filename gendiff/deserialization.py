import json
import yaml


def deserialize(file_path):
    if file_path.endswith('.yaml') or file_path.endswith('.yml'):
        with open(file_path) as file_path:
            return yaml.safe_load(file_path)
    elif file_path.endswith('.json'):
        with open(file_path) as file_path:
            return json.load(file_path)
    else:
        raise Exception('Invalid format')

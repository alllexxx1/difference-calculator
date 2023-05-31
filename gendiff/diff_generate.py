import json


def generate_diff(file1, file2):
    with (
        open(file1) as file1,
        open(file2) as file2,
    ):
        json1 = json.load(file1)
        json2 = json.load(file2)

    diff = find_diff(json1, json2)
    diff_str = format_diff(diff)

    return diff_str


def find_diff(obj1, obj2):
    diff = {}

    for key, value in obj1.items():
        if key not in obj2 or value != obj2[key]:
            diff[f'- {key}'] = str(value)

    for key, value in obj2.items():
        if key not in obj1 or value != obj1[key]:
            diff[f'+ {key}'] = str(value)
        else:
            diff[f'  {key}'] = str(value)

    sorted_diff = {k: diff[k] for k in sorted(diff, key=lambda x: x[2])}
    return sorted_diff


def format_diff(diff, indent=2):
    diff_str = '{\n'
    for key, value in diff.items():
        diff_str += ' ' * indent + f'{key}: {value.lower()}\n'
    diff_str += '}'
    return diff_str

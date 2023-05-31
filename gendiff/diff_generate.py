from gendiff.deserialization import deserialize_format


def generate_diff(file1, file2):
    file1 = deserialize_format(file1)
    file2 = deserialize_format(file2)

    diff = find_diff(file1, file2)
    diff_str = format_diff(diff)

    return diff_str


def find_diff(obj1, obj2):
    diff = {}

    for key, value in obj1.items():
        if key not in obj2 or value != obj2[key]:
            diff[f'- {key}'] = normalize_value(value)

    for key, value in obj2.items():
        if key not in obj1 or value != obj1[key]:
            diff[f'+ {key}'] = normalize_value(value)
        else:
            diff[f'  {key}'] = normalize_value(value)
    sorted_diff = {k: diff[k] for k in sorted(diff, key=lambda x: x[2])}
    return sorted_diff


def format_diff(diff, indent=2):
    diff_str = '{\n'
    for key, value in diff.items():
        diff_str += ' ' * indent + f'{key}: {value}\n'
    diff_str += '}'
    return diff_str


def normalize_value(value):
    if value in (False, True):
        return str(value).lower()
    elif value is None:
        return 'null'
    return str(value)


# print(generate_diff('/home/aleksei/python-project-50/tests/fixtures/file1.yaml',
# '/home/aleksei/python-project-50/tests/fixtures/file2.yaml'))

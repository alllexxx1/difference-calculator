from gendiff.deserialization import load_file
from gendiff.find_diff import find_diff
from gendiff.formatters.stylish import get_stylish
from gendiff.formatters.plain import get_plain
from gendiff.formatters.json_ import get_json


def generate_diff(file_path1, file_path2, formatter='stylish'):
    file_path1 = load_file(file_path1)
    file_path2 = load_file(file_path2)

    diff = find_diff(file_path1, file_path2)
    format_diff = make_format(diff, formatter)

    return format_diff


def make_format(data, formatter):
    if formatter == 'plain':
        return get_plain(data)
    elif formatter == 'json':
        return get_json(data)
    elif formatter == 'stylish':
        return get_stylish(data)
    else:
        raise Exception('Invalid formatter!')

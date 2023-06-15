from gendiff.deserialization import deserialize
from gendiff.find_diff import find_diff
from gendiff.formatters.stylish import get_stylish
from gendiff.formatters.plain import get_plain
from gendiff.formatters.json_mapping import get_json


def generate_diff(file1, file2, formatter='stylish'):
    file1 = deserialize(file1)
    file2 = deserialize(file2)

    diff = find_diff(file1, file2)
    format_diff = to_format(diff, formatter)

    return format_diff


def to_format(data, formatter):
    if formatter == 'plain':
        return get_plain(data)
    elif formatter == 'json':
        return get_json(data)
    return get_stylish(data)

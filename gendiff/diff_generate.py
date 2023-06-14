from gendiff.deserialization import deserialize
from gendiff.find_diff import find_diff
from gendiff.formatters.stylish import get_stylish
from gendiff.formatters.plain import get_plain


def generate_diff(file1, file2, formatter='stylish'):
    file1 = deserialize(file1)
    file2 = deserialize(file2)

    diff = find_diff(file1, file2)
    format_diff = to_format(diff, formatter)

    return format_diff


def to_format(data, formatter):
    if formatter == 'stylish':
        format_data = get_stylish(data)
    elif formatter == 'plain':
        format_data = get_plain(data)
    return format_data


# print(generate_diff('/home/aleksei/python-project-50/tests/fixtures/input/flat1.yaml',
# '/home/aleksei/python-project-50/tests/fixtures/input/flat2.yaml', 'plain'))

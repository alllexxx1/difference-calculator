INDENT_COUNT = 4


def get_stylish(data):
    return make_diff(data, depth=1)


def make_diff(current_data, depth):
    if not isinstance(current_data, (list, dict)):
        return str(current_data)
    lines = make_lines(current_data, depth, replacer=' ')
    return '\n'.join(lines)


def make_lines(current_data, depth, replacer=' '):
    indent1 = replacer * ((INDENT_COUNT * depth) - 2)
    indent2 = replacer * INDENT_COUNT * depth
    closing_indent = replacer * INDENT_COUNT * (depth - 1)
    lines = []

    if isinstance(current_data, dict):
        for k, v in current_data.items():
            lines.append(f'{indent2}{k}: {make_diff(v, depth=depth + 1)}')
    for diff in current_data:
        add_lines(diff, indent1, indent2, depth, lines)

    result = ['{'] + lines + [closing_indent + '}']
    return result


def add_lines(diff, indent1, indent2, depth, lines):
    status = get_status(diff)
    if status == 'deleted':
        add_deleted(diff, indent1, depth, lines)
    elif status == 'added':
        add_added(diff, indent1, depth, lines)
    elif status == 'unchanged':
        add_unchanged(diff, indent2, depth, lines)
    elif status == 'changed':
        add_changed(diff, indent1, depth, lines)
    elif status == 'parent':
        add_parent(diff, indent2, depth, lines)


def add_deleted(diff, indent1, depth, lines):
    value = normalize_value(diff['value'])
    key = '- ' + diff['key']
    lines.append(
        f'{indent1}{key}: {make_diff(value, depth=depth + 1)}'
    )


def add_added(diff, indent1, depth, lines):
    value = normalize_value(diff['value'])
    key = '+ ' + diff['key']
    lines.append(
        f'{indent1}{key}: {make_diff(value, depth=depth + 1)}'
    )


def add_unchanged(diff, indent2, depth, lines):
    value = normalize_value(diff['value'])
    key = diff['key']
    lines.append(
        f'{indent2}{key}: {make_diff(value, depth=depth + 1)}'
    )


def add_changed(diff, indent1, depth, lines):
    value1 = normalize_value(diff['value1'])
    value2 = normalize_value(diff['value2'])
    key1 = '- ' + diff['key']
    key2 = '+ ' + diff['key']
    lines.append(
        f'{indent1}{key1}: {make_diff(value1, depth=depth + 1)}'
    )
    lines.append(
        f'{indent1}{key2}: {make_diff(value2, depth=depth + 1)}'
    )


def add_parent(diff, indent2, depth, lines):
    children = normalize_value(diff['children'])
    key = diff['key']
    lines.append(
        f'{indent2}{key}: {make_diff(children, depth=depth + 1)}'
    )


def get_status(diff):
    if 'status' in diff:
        return diff['status']


def normalize_value(value):
    if value in (False, True):
        value = str(value).lower()
    elif value is None:
        value = 'null'
    elif isinstance(value, dict):
        for v in value.values():
            v = normalize_value(v)
    return value

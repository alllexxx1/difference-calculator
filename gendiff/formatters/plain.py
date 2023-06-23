def get_plain(data):
    return display_diff(data)


def display_diff(current_data, path=''):
    lines = []
    for diff in current_data:
        status = diff['status']
        if status == 'deleted':
            key = diff['key']
            lines.append(f"Property '{path}{key}' was removed")
        elif status == 'added':
            value = normalize_value(diff['value'])
            key = diff['key']
            lines.append(
                f"Property '{path}{key}' was added with value: {value}"
            )
        elif status == 'changed':
            value1 = normalize_value(diff['value1'])
            value2 = normalize_value(diff['value2'])
            key = diff['key']
            lines.append(
                f"Property '{path}{key}' was updated. From {value1} to {value2}"
            )
        elif status == 'parent':
            children = diff['value']
            key = diff['key']
            lines.append(display_diff(children, path=path + f'{key}.'))
    result = '\n'.join(lines)
    return result


def normalize_value(value):
    if isinstance(value, dict):
        value = '[complex value]'
    elif value in (False, True):
        value = str(value).lower()
    elif value is None:
        value = 'null'
    elif isinstance(value, int):
        value = str(value)
    else:
        value = f"'{value}'"
    return value

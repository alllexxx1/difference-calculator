from itertools import chain


def get_stylish(data, replacer=' ', indent_count=4):  # noqa: C901
    def walk(current_data, depth):
        if not isinstance(current_data, (list, dict)):
            return str(current_data)
        indent_size1 = depth * indent_count + 2
        indent_size2 = depth * indent_count + 4
        indent1 = replacer * indent_size1
        indent2 = replacer * indent_size2
        current_indent = replacer * depth * indent_count
        lines = []
        if isinstance(current_data, dict):
            for k, v in current_data.items():
                lines.append(f'{indent2}{k}: {walk(v, depth + 1)}')
        for diff in current_data:
            if 'status' in diff:
                status = diff['status']
                if status == 'deleted':
                    value = normalize_value(diff['value'])
                    key = '- ' + diff['key']
                    lines.append(
                        f'{indent1}{key}: {walk(value, depth + 1)}'
                    )
                elif status == 'added':
                    value = normalize_value(diff['value'])
                    key = '+ ' + diff['key']
                    lines.append(
                        f'{indent1}{key}: {walk(value, depth + 1)}'
                    )
                elif status == 'unchanged':
                    value = normalize_value(diff['value'])
                    key = diff['key']
                    lines.append(
                        f'{indent2}{key}: {walk(value, depth + 1)}'
                    )
                elif status == 'changed':
                    value1 = normalize_value(diff['value1'])
                    value2 = normalize_value(diff['value2'])
                    key1 = '- ' + diff['key']
                    key2 = '+ ' + diff['key']
                    lines.append(
                        f'{indent1}{key1}: {walk(value1, depth + 1)}'
                    )
                    lines.append(
                        f'{indent1}{key2}: {walk(value2, depth + 1)}'
                    )
                elif status == 'parent':
                    children = normalize_value(diff['value'])
                    key = diff['key']
                    lines.append(
                        f'{indent2}{key}: {walk(children, depth + 1)}'
                    )
            else:
                pass
        result = chain('{', lines, [current_indent + '}'])
        return '\n'.join(result)
    return walk(data, 0)


def normalize_value(value):
    if value in (False, True):
        value = str(value).lower()
    elif value is None:
        value = 'null'
    elif isinstance(value, dict):
        for v in value.values():
            v = normalize_value(v)
    return value

import jso


def get_json(data):
    lines = json.dumps(data, indent=4)
    return '\n'.join(lines)

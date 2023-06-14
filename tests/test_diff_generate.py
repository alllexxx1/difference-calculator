import pytest
from gendiff import generate_diff


FLAT_JSON1 = './tests/fixtures/input/flat1.json'
FLAT_JSON2 = './tests/fixtures/input/flat2.json'
FLAT_YAML1 = './tests/fixtures/input/flat1.yaml'
FLAT_YAML2 = './tests/fixtures/input/flat2.yaml'

NESTED_JSON1 = './tests/fixtures/input/nested1.json'
NESTED_JSON2 = './tests/fixtures/input/nested2.json'
NESTED_YAML1 = './tests/fixtures/input/nested1.yaml'
NESTED_YAML2 = './tests/fixtures/input/nested2.yaml'

STYLISH_FLAT_JSON = './tests/fixtures/output/flat_json.txt'
STYLISH_FLAT_YAML = './tests/fixtures/output/flat_yaml.txt'
STYLISH_NESTED = './tests/fixtures/output/stylish_nested.txt'


@pytest.mark.parametrize('input1, input2, output', [
    (FLAT_JSON1, FLAT_JSON2, STYLISH_FLAT_JSON),
    (FLAT_YAML1, FLAT_YAML2, STYLISH_FLAT_YAML),
    (NESTED_JSON1, NESTED_JSON2, STYLISH_NESTED),
    (NESTED_YAML1, NESTED_YAML2, STYLISH_NESTED)
])
def test_generate_diff(input1, input2, output):
    with open(output) as file:
        expected_diff = file.read()
    assert generate_diff(input1, input2) == expected_diff

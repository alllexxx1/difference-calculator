from gendiff import generate_diff


def test_generate_diff_json_format():
    with open('./tests/fixtures/right_json_format1.txt') as f:
        expected_diff = f.read()
    assert generate_diff('./tests/fixtures/file1.json',
                         './tests/fixtures/file2.json') == expected_diff


def test_generate_diff_json_format_for_the_same_files():
    with open('./tests/fixtures/right_json_format2.txt') as f:
        expected_diff = f.read()
    assert generate_diff('./tests/fixtures/file1.json',
                         './tests/fixtures/file1.json') == expected_diff


def test_generate_diff_yaml_format():
    with open('./tests/fixtures/right_yaml_format.txt') as f:
        expected_diff = f.read()
    assert generate_diff('./tests/fixtures/file1.yaml',
                         './tests/fixtures/file2.yaml') == expected_diff

from gendiff import generate_diff


def test_generate_diff():
    with open('./tests/fixtures/test_string.txt') as f:
        result_str = f.read()
        assert generate_diff('./tests/fixtures/file1.json',
                             './tests/fixtures/file2.json') == result_str

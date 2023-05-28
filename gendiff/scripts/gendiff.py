#!/usr/bin/env python3


from gendiff.parser import get_parser
# from gendiff import generate_diff


def main():
    print(get_parser())
    # print(
    #     generate_diff(
    #         file1='gendiff.file1.json',
    #         file2='gendiff.file2.json',
    #     )
    # )


if __name__ == '__main__':
    main()

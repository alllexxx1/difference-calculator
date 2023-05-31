#!/usr/bin/env python3


from gendiff.parser import get_parser
from gendiff import generate_diff


def main():
    args = get_parser().parse_args()
    print(generate_diff(args.first_file, args.second_file))


if __name__ == '__main__':
    main()

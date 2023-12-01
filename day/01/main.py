import argparse
import os
import sys

from src import *


def read_input(inp_path: str) -> list:
    with open(inp_path) as f:
        inp = f.read().splitlines()
        return inp


if __name__ == '__main__':
    ############################ v DEBUG BLOCK v ############################

    # script_dir = os.path.dirname(os.path.abspath(__file__))
    # input_path = os.path.join(script_dir, 'input', 'input.txt')
    # input_raw = read_input(input_path)
    # result = part_2.run(input_raw)
    # sys.exit()

    ############################ ^ DEBUG BLOCK ^ ############################

    parser = argparse.ArgumentParser(description='Advent of code 2023')
    parser.add_argument(
        'part', type=int, help='Provide the part you want to run - either 1 or 2'
    )
    parser.add_argument(
        '--test', type=int, help='Set flag to run the test-file against provided input'
    )
    args = parser.parse_args()

    if args.part is None:
        print('No part has been chosen')
        sys.exit()

    if args.part not in [1, 2]:
        print(f'{args.part} is not a valid part')
        sys.exit()

    part = args.part
    is_test = False
    assert_value = 0
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_path = os.path.join(script_dir, 'input', 'input.txt')

    if args.test is not None:
        is_test = True
        assert_value = args.test

    if is_test:
        input_path = os.path.join(script_dir, 'input', 'test.txt')

    input_raw = read_input(input_path)
    result = None

    if part == 1:
        result = part_1.run(input_raw)

    if part == 2:
        result = part_2.run(input_raw)

    if is_test:
        print(f'Asserting {assert_value}')
        assert result == assert_value, f'Expected {assert_value} but got {result}'
        print('Assertion successful')
    else:
        print(result)

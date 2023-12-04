import re


from functools import cache


def get_card_number(input_line: str) -> int:
    return int(re.search(r'(\d+)\:', input_line).group(1))


def get_winning_numbers(input_line: str) -> set:
    return set(re.findall('\d{1,2}', re.search(r':\s(.*?)\s\|', input_line).group(1)))


def get_drawn_numbers(input_line: str) -> set:
    return set(re.findall('\d{1,2}', re.search(r'\|\s(.*?)$', input_line).group(1)))


@cache
def calculate_points(matching_numbers: int) -> int:
    return 2 ** (matching_numbers - 1)

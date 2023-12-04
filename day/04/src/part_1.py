import re

from . import utils


def run(inp):
    points = 0

    for line in inp:
        winning_numbers = set(re.findall('\d{1,2}', re.search(r':\s(.*?)\s\|', line).group(1)))
        drawn_numbers = set(re.findall('\d{1,2}', re.search(r'\|\s(.*?)$', line).group(1)))
        result = winning_numbers & drawn_numbers

        if (num_right := len(result)) > 0:
            points += 2**(num_right - 1)

    return points

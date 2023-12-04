from .utils import *


def run(inp):
    points = 0

    for line in inp:
        winning_numbers = get_winning_numbers(line)
        drawn_numbers = get_drawn_numbers(line)
        result = winning_numbers & drawn_numbers

        if (num_match := len(result)) > 0:
            points += calculate_points(num_match)

    return points

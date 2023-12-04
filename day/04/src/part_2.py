from .utils import *


def run(inp):
    card_dict: dict = {}

    for line in inp:
        card_number = get_card_number(line)

        if card_number in card_dict:
            card_dict[card_number] += 1
        else:
            card_dict[card_number] = 1

        winning_numbers = get_winning_numbers(line)
        drawn_numbers = get_drawn_numbers(line)
        num_right = len(winning_numbers & drawn_numbers)

        for num in range(card_number + 1, card_number + num_right + 1):
            if num in card_dict:
                card_dict[num] += card_dict[card_number]
            else:
                card_dict[num] = card_dict[card_number]

    return sum(card_dict.values())

import re

from . import utils


def run(inp):
    card_dict: dict = {}

    for line in inp:
        card_number = int(re.search(r'(\d+)\:', line).group(1))

        if card_number in card_dict:
            card_dict[card_number] += 1
        else:
            card_dict[card_number] = 1

        winning_numbers = set(re.findall('\d{1,2}', re.search(r':\s(.*?)\s\|', line).group(1)))
        drawn_numbers = set(re.findall('\d{1,2}', re.search(r'\|\s(.*?)$', line).group(1)))
        num_right = len(winning_numbers & drawn_numbers)

        for num in range(card_number + 1, card_number + num_right + 1):
            if num in card_dict:
                card_dict[num] += card_dict[card_number]
            else:
                card_dict[num] = card_dict[card_number]

    return sum(card_dict.values())

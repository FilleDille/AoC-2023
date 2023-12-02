from . import utils
import numpy as np


def run(inp):
    threshold: dict = {'red': 12, 'green': 13, 'blue': 14}
    game_list: list = []

    for line in inp:
        game_list.append(utils.Game(line, threshold))

    prod_of_id = sum([np.prod(list(x.max_dict.values())) for x in game_list])

    return prod_of_id

from . import utils


def run(inp):
    threshold: dict = {'red': 12, 'green': 13, 'blue': 14}
    game_list: list = []

    for line in inp:
        game_list.append(utils.Game(line, threshold))

    filtered_game_list = list(filter(lambda x: x.valid_game, game_list))
    sum_of_id = sum(x.id for x in filtered_game_list)

    return sum_of_id

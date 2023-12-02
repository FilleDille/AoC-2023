import re


class Game:
    def __init__(self, input_line: str, threshold: dict):
        self.threshold = threshold
        self.max_dict: dict = {}
        self.id: int = self.extract_id(input_line)
        self.sets: list = self.extract_sets(input_line)
        self.valid_game: bool = True
        self.check_if_valid()

    def check_if_valid(self):
        self.max_dict = {
            'red': max([x['red'] for x in self.sets]),
            'green': max([x['green'] for x in self.sets]),
            'blue': max([x['blue'] for x in self.sets])
        }

        for color, val in self.max_dict.items():
            if val > self.threshold[color]:
                self.valid_game = False
                return

    @staticmethod
    def extract_id(input_line: str) -> int:
        return int(input_line.split(':')[0].split(' ')[1])

    @staticmethod
    def extract_sets(input_line: str) -> list:
        sets = input_line.split(':')[1].strip()
        set_list_raw = sets.split(';')
        set_list = []

        for set_line in set_list_raw:
            set_list.append(Game.extract_colors(set_line))

        return set_list

    @staticmethod
    def extract_colors(set_line: str) -> dict:
        set_dict = {'red': 0, 'green': 0, 'blue': 0}
        regex_search = re.finditer(r'(\d+) (red|green|blue)', set_line)

        for found_match in regex_search:
            set_dict[found_match.group(2)] = int(found_match.group(1))

        return set_dict

from .utils import *


def run(inp):
    time_int: int = fetch_int(inp[0])
    distance_record_int: int = fetch_int(inp[1])
    ways_to_win: int = 1
    divisor = 2 if time_int % 2 == 1 else 1
    time_length = np.ceil(time_int / divisor)

    time_array = np.arange(time_length)
    time_left_array = time_int - time_array
    distance_traveled_array = time_array * time_left_array
    ways_to_win = np.count_nonzero(distance_traveled_array > distance_record_int)

    return ways_to_win * divisor

from .utils import *


def run(inp):
    time_int: int = fetch_int(inp[0])
    distance_record_int: int = fetch_int(inp[1])
    ways_to_win: int = 1

    time_array = np.arange(time_int + 1)
    time_left_array = time_int - time_array
    distance_traveled_array =  time_array * time_left_array
    ways_to_win = np.count_nonzero(distance_traveled_array > distance_record_int)

    return ways_to_win

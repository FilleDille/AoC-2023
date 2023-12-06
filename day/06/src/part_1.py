from .utils import *


def run(inp):
    time_list: list = fetch_list(inp[0])
    distance_record_list: list = fetch_list(inp[1])
    ways_to_win: int = 1

    for i in range(len(time_list)):
        time_array = np.arange(time_list[i] + 1)
        time_left_array = time_list[i] - time_array
        distance_traveled_array =  time_array * time_left_array
        ways_to_win *= np.count_nonzero(distance_traveled_array > distance_record_list[i])

    return ways_to_win

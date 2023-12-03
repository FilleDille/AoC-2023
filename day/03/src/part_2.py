import numpy as np
import re


from . import utils


def run(inp):
    num_span_list: list = []
    num_group_list: list = []
    char_index_list: list = []

    for index, inp_line in enumerate(inp):
        regex_search = re.finditer(r'\b(\d+)\b', inp_line)

        for found_match in regex_search:
            num_span_list.append([index, found_match.span()[0], found_match.span()[1] - 1])
            num_group_list.append(int(found_match.group()))

        regex_search = re.finditer(r'\*', inp_line)

        for found_match in regex_search:
            char_index_list.append([index, found_match.span()[0], found_match.span()[1] - 1])

    np_numbers = np.array(num_span_list)
    prod_list = []

    for spec_char in char_index_list:
        dist_from_current_char = np.abs(np_numbers - np.array(spec_char))
        np_index_distance = dist_from_current_char[:, 0] <= 1
        np_span_distance = dist_from_current_char[:, 1:] <= 1
        combined_mask = np.concatenate([np_index_distance[:, np.newaxis], np_span_distance], axis=1)
        indices = np.where((combined_mask[:, 0] == 1) & ((combined_mask[:, 1] == 1) | (combined_mask[:, 2] == 1)))
        num_list: list = []

        if len(indices[0]) == 2:
            for index in indices[0]:
                num_list.append(num_group_list[index])

        if len(num_list) > 0:
            prod_list.append(num_list[0] * num_list[1])

    sum_of_prod = sum(prod_list)

    return sum_of_prod

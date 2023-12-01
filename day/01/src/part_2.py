import re


num_dict = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }


def run(inp) -> int:
    transformed_inp = [transform(x) for x in inp]
    inp_int_only = [''.join(re.findall('[0-9]', x)) for x in transformed_inp]
    inp_two_ints = [int(x[0] + x[-1]) for x in inp_int_only]
    sum_calibration_values = sum(inp_two_ints)
    return sum_calibration_values


def transform(inp_line: str) -> str:
    transformed_line = inp_line
    pattern = r'(?=(one|two|three|four|five|six|seven|eight|nine))'
    regex_search = re.findall(pattern, transformed_line)

    for found_match in regex_search:
        transformed_line = transformed_line.replace(found_match, num_dict[found_match])

    while regex_search:
        transformed_line = transformed_line.replace(regex_search.group(), num_dict[regex_search.group()])
        regex_search = re.search(pattern, transformed_line)

    return transformed_line

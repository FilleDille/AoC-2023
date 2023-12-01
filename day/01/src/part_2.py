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

pattern = r'(?=(one|two|three|four|five|six|seven|eight|nine))'


def run(inp) -> int:
    transformed_inp = [transform(x) for x in inp]
    translated_inp = [translate(x) for x in transformed_inp]
    inp_int_only = [''.join(re.findall('[0-9]', x)) for x in translated_inp]
    inp_two_ints = [int(x[0] + x[-1]) for x in inp_int_only]
    sum_calibration_values = sum(inp_two_ints)
    return sum_calibration_values


def transform(inp_line: str) -> str:
    transformed_line = inp_line
    regex_search = re.finditer(pattern, transformed_line)
    span_list = []

    for found_match in regex_search:
        keyword = found_match.group(1)
        start_pos = found_match.start()
        span_list.append((keyword, start_pos, start_pos + len(keyword) - 1))

    for i in range(len(span_list) - 1):
        if span_list[i][2] >= span_list[i + 1][1]:
            first_part_of_overlap = span_list[i][0]
            last_char = first_part_of_overlap[-1]
            edited_first_part = ''.join((first_part_of_overlap, last_char))
            transformed_line = transformed_line.replace(first_part_of_overlap, edited_first_part)

    return transformed_line


def translate(inp_line: str) -> str:
    translated_line = inp_line

    for k, v in num_dict.items():
        if k in translated_line:
            translated_line = translated_line.replace(k, v)

    return translated_line

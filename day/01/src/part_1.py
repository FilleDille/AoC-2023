import re


def run(inp):
    inp_int_only = [''.join(re.findall('[0-9]', x)) for x in inp]
    inp_two_ints = [int(x[0] + x[-1]) for x in inp_int_only]
    sum_calibration_values = sum(inp_two_ints)
    return sum_calibration_values

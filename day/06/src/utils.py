import numpy as np


def fetch_list(inp_line: str) -> list:
    return [int(i) for i in inp_line.split(':')[1].strip().split()]


def fetch_int(inp_line: str) -> int:
    return int(inp_line.split(':')[1].replace(' ', ''))

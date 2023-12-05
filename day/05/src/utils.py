import pandas as pd


def create_tables(inp: list) -> dict:
    table_dict: dict = {}
    dest_list: list = []
    source_list: list = []
    range_list: list = []
    table_name: str = ''
    i: int = 0

    for line in inp[2:]:
        if ':' in line:
            # table_name = line[:-1].split()[0]
            table_name = i
            i += 1
            continue

        if line == '' or line == '.':
            table_dict[table_name] = {
                'destination': dest_list.copy(),
                'source_lower_bound': source_list.copy(),
                'range': range_list.copy()
            }

            dest_list.clear()
            source_list.clear()
            range_list.clear()
            continue

        dest, source, rng = line.split()
        dest_list.append(int(dest))
        source_list.append(int(source))
        range_list.append(int(rng))

    return table_dict


def create_dataframes(inp: dict) -> dict:
    df_dict: dict = {}

    for table_name, value_dict in inp.items():
        df_dict[table_name] = pd.DataFrame(value_dict)

    return df_dict


def fetch_seeds(inp: str) -> list:
    return list(map(lambda x: int(x.strip()), inp.split(':')[1].split()))

from .utils import *


def run(inp):
    seeds = fetch_seeds(inp[0])
    location_list: list = []
    table_dict = create_tables(inp)
    df_dict = create_dataframes(table_dict)

    for table_name, df in df_dict.items():
        df_dict[table_name]['destination_diff'] = df['destination'] - df['source_lower_bound']
        df_dict[table_name]['source_upper_bound'] = df['source_lower_bound'] + df['range'] - 1

    for seed in seeds:
        transformed_seed = seed

        for i in range(len(df_dict)):
            df = df_dict[i]
            df_filtered = df[(df['source_lower_bound'] <= transformed_seed) & (df['source_upper_bound'] >= transformed_seed)]

            if len(df_filtered) > 0:
                transformed_seed = transformed_seed + df_filtered['destination_diff'].values[0]
            else:
                transformed_seed = transformed_seed

        location_list.append(transformed_seed)

    return min(location_list)

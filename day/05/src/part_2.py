import pandas as pd

from .utils import *


def run(inp):
    locations = [i for i in range(65_000_000, 70_000_000)]
    location_min: int = 0
    seeds: list = fetch_seeds(inp[0])
    seed_boundaries: dict = {
        'lower_bound': [seeds[i] for i in range(len(seeds)) if i % 2 == 0],
        'addon': [seeds[i] for i in range(len(seeds)) if i % 2 == 1]
    }

    df_seed = pd.DataFrame(seed_boundaries)
    df_seed['upper_bound'] = df_seed['lower_bound'] + df_seed['addon'] - 1

    table_dict = create_tables(inp)
    df_dict = create_dataframes(table_dict)

    for table_name, df in df_dict.items():
        df_dict[table_name]['destination_diff'] = df['destination'] - df['source_lower_bound']
        df_dict[table_name]['destination_upper_bound'] = df['destination'] + df['range'] - 1

    for location in locations:
        transformed_location = location

        for i in reversed(range(len(df_dict))):
            df = df_dict[i]
            df_filtered = df[(df['destination'] <= transformed_location) & (df['destination_upper_bound'] >= transformed_location)]

            if len(df_filtered) > 0:
                transformed_location = transformed_location - df_filtered['destination_diff'].values[0]
            else:
                transformed_location = transformed_location

        df_seed_filtered = df_seed[(df_seed['lower_bound'] <= transformed_location) & (df_seed['upper_bound'] >= transformed_location)]

        if len(df_seed_filtered) > 0:
            return location

    return None

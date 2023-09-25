import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    # Create a filter to identify big countries either by area or by population
    big_countries_filter = (world['area'] >= 3000000) | (world['population'] >= 25000000)
    # Apply the filter to the dataframe and select the desired columns
    big_countries_df = world[big_countries_filter][['name', 'population', 'area']]
    return big_countries_df

# # Assuming 'world_data.csv' contains the World table data
# world_df = pd.read_csv('world_data.csv')

# # Call the function and store the result in a new dataframe
# big_countries_df = big_countries(world_df)
# print(big_countries_df)

    
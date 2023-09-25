import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    # Filtering the DataFrame based on the conditions
    filtered_products = products[(products['low_fats'] == 'Y') & (products['recyclable'] == 'Y')][['product_id']]
    return filtered_products

# Explanation

# Single Square Brackets []: When you use single square brackets with a string (e.g., df['product_id']), you are selecting a single column from the DataFrame, and the result is a Series.
# Double Square Brackets [[]]: When you use double square brackets with a string inside (e.g., df[['product_id']]), you are still selecting a single column, but the result is a DataFrame.
# Here are the differences between the two in more detail:
# df['product_id'] will return a Series which is a one-dimensional labeled array.
# df[['product_id']] will return a DataFrame which is a two-dimensional labeled data structure.
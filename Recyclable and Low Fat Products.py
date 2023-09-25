import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    # Filtering the DataFrame based on the conditions
    filtered_products = products[(products['low_fats'] == 'Y') & (products['recyclable'] == 'Y')][['product_id']]
    return filtered_products
import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    # Merge the two dataframes on the customer id, using a left join to keep all customers
    merged_df = pd.merge(customers, orders, left_on='id', right_on='customerId', how='left')
    # Filter the merged dataframe to only include rows where the order id is null
    no_order_customers = merged_df[merged_df['id_y'].isnull()][['name']]
    # Rename the columns for clarity
    no_order_customers.columns = ['Customers']
    return no_order_customers

#This line of code is using the pd.merge() function from the pandas library to merge two DataFrames, customers and orders, on a specified key. Let's break down the parameters used in this function call:

#customers and orders: These are the two DataFrames being merged.

#left_on='id': This parameter specifies the column in the customers DataFrame to use as the key for the merge.

# right_on='customerId': This parameter specifies the column in the orders DataFrame to use as the key for the merge.

#how='left': This parameter specifies the type of merge to perform. In this case, a left merge (or left join) is being performed. This means that all the rows from the customers DataFrame will be included in the merged DataFrame, merged_df. For rows in customers that have a matching key in orders, the columns from orders will be included in merged_df. For rows in customers that do not have a matching key in orders, the columns from orders will have null values in merged_df.
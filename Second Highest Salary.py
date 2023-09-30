# Importing the necessary library
import pandas as pd

# Defining a function named 'second_highest_salary', which accepts a DataFrame 'employee' as an argument and returns a DataFrame
def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    
    # From the 'employee' DataFrame, select the 'salary' column and remove duplicate values. 
    # This line results in a pandas Series of unique salaries.
    unique_salaries = employee['salary'].drop_duplicates()
    
    # Sort the unique salaries in descending order. This will still be a pandas Series, 
    # but now it's sorted from highest to lowest salary.
    sorted_salaries = unique_salaries.sort_values(ascending=False)
    
    # Check if there are less than 2 unique salaries (meaning there's no second highest salary).
    # If so, return a DataFrame with a single column 'SecondHighestSalary' and a single row with a value of None.
    if len(sorted_salaries) < 2:
        return pd.DataFrame({'SecondHighestSalary': [None]})
    
    # If there are at least 2 unique salaries, 
    # get the second highest salary by accessing the value at index 1 of the sorted salaries Series.
    second_highest = sorted_salaries.iloc[1]
    
    # Create and return a DataFrame with a single column 'SecondHighestSalary' and a single row containing the second highest salary.
    # The [second_highest] is a list containing the single value of the second highest salary.
    # We're passing a dictionary to the DataFrame constructor, where the key is the column name 
    # and the value is a list containing the data for that column.
    return pd.DataFrame({'SecondHighestSalary': [second_highest]})

# Now you can call the function, passing in your employee DataFrame.
# Example:
# employee_df = pd.DataFrame({'id': [1, 2, 3], 'salary': [100, 200, 300]})
# result_df = second_highest_salary(employee_df)
# print(result_df)

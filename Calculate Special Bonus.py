import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    # Create a copy of the input DataFrame to avoid altering the original DataFrame
    employees_copy = employees.copy()
    
    # Initialize a new column for bonus with a default value of 0
    employees_copy['bonus'] = 0
    
    # Identify employees with odd employee_id and names not starting with 'M'
    bonus_employees = employees_copy[(employees_copy["employee_id"] % 2 != 0) & (~employees_copy["name"].str.startswith("M"))]
    
    # Update the bonus column for the eligible employees
    employees_copy.loc[bonus_employees.index, 'bonus'] = bonus_employees['salary']
    
    # Sort by employee_id
    result = employees_copy.sort_values(by='employee_id')[['employee_id', 'bonus']]
    
    return result
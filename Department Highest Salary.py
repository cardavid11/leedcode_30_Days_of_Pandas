import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    # Step 1: Identify the maximum salary for each department.
    # The transform method broadcasts the result of 'max' back to the original number of rows in 'employee'.
    employee['max_salary'] = employee.groupby('departmentId')['salary'].transform('max')
    print(employee['max_salary'])

    # Here's a step-by-step visual explanation based on a simplified DataFrame:
    #     Original DataFrame:
    # | id | name  | salary | departmentId |
    # |----|-------|--------|--------------|
    # | 1  | Joe   | 70000  | 1            |
    # | 2  | Jim   | 90000  | 1            |
    # | 3  | Henry | 80000  | 2            |
    # | 4  | Sam   | 60000  | 2            |

    # After Grouping and Selection:
    # Group 1 (departmentId = 1): salary = [70000, 90000]
    # Group 2 (departmentId = 2): salary = [80000, 60000]

    # After Transformation:
    # Series:
    # 0    90000  (from group 1)
    # 1    90000  (from group 1)
    # 2    80000  (from group 2)
    # 3    80000  (from group 2)

    # After Assignment:
    # DataFrame:
    # | id | name  | salary | departmentId | max_salary |
    # |----|-------|--------|--------------|------------|
    # | 1  | Joe   | 70000  | 1            | 90000      |
    # | 2  | Jim   | 90000  | 1            | 90000      |
    # | 3  | Henry | 80000  | 2            | 80000      |
    # | 4  | Sam   | 60000  | 2            | 80000      |

    # Step 2: Filter the rows where the salary equals the maximum salary for the department.
    # This will keep all instances of maximum salaries, as there might be more than one per department.
    highest_salary_employees = employee[employee['salary'] == employee['max_salary']]
    # This employee['salary'] == employee['max_salary'] give me a Series of True/False values, which is used to filter the DataFrame.

    # Step 3: Merge the filtered employee data with the department data to get department names.
    # The merge is performed on the 'id' column of 'department' and the 'departmentId' column of 'employee'.
    result = pd.merge(highest_salary_employees, department, left_on='departmentId', right_on='id', suffixes=('', '_dept'))

    # Function Call: pd.merge is the function being called to perform the merge operation between the two DataFrames.
    # highest_salary_employees: This is the first (or left) DataFrame involved in the merge.
    # department: This is the second (or right) DataFrame involved in the merge.
    # Keys for Merge:
    # left_on='departmentId': This argument specifies the column from the left DataFrame (highest_salary_employees) to use as the key for the merge.
    # right_on='id': This argument specifies the column from the right DataFrame (department) to use as the key for the merge.
    # The merge operation will align rows based on the values in these specified key columns.
    # Suffixes:
    # suffixes=('', '_dept'): This argument specifies the suffixes to append to overlapping column names in the left and the right DataFrames, respectively. In this case, it's telling pandas to keep the original column name from the left DataFrame and append _dept to the overlapping column name from the right DataFrame.
        
    # Step 4: Select and rename the desired columns to match the output format.
    result = result[['name_dept', 'name', 'salary']]
    result.columns = ['Department', 'Employee', 'Salary']
    
    # Step 5: Drop the 'max_salary' column from the 'employee' DataFrame as it's no longer needed.
    employee.drop(columns='max_salary', inplace=True)
    
    return result

# Creating the Employee DataFrame
employee_data = {
    'id': [1, 2, 3, 4, 5],
    'name': ['Joe', 'Jim', 'Henry', 'Sam', 'Max'],
    'salary': [70000, 90000, 80000, 60000, 90000],
    'departmentId': [1, 1, 2, 2, 1]
}
employee = pd.DataFrame(employee_data)

# Creating the Department DataFrame
department_data = {
    'id': [1, 2],
    'name': ['IT', 'Sales']
}
department = pd.DataFrame(department_data)

# Now you can pass these DataFrames to the department_highest_salary function
result_df = department_highest_salary(employee, department)
print(result_df)

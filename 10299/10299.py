https://platform.stratascratch.com/coding/10299-finding-updated-records?code_type=2

# Import your libraries
import pandas as pd

# Start writing code
ms_employee_salary.head()
results = ms_employee_salary.sort_values(['id','salary',], ascending = [True, False]).drop_duplicates('id')

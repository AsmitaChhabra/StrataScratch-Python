# https://platform.stratascratch.com/coding/9972-find-the-base-pay-for-police-captains?code_type=2

# Import your libraries
import pandas as pd

# Start writing code


sf_public_salaries.sort_values('jobtitle', ascending = False)

filtercpatain = sf_public_salaries[sf_public_salaries['jobtitle'].str.contains('CAPTAIN')]
filtercpatain[['employeename', 'basepay']]

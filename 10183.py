https://platform.stratascratch.com/coding/10183-total-cost-of-orders?code_type=2

# Import your libraries
import pandas as pd

# Start writing code

merged = pd.merge(customers, orders, left_on='id', right_on='cust_id')
result = merged.groupby(['cust_id','first_name'])['total_order_cost'].sum().reset_index()

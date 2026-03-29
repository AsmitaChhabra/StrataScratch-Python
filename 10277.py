#https://platform.stratascratch.com/coding/10277-find-all-inspections-which-are-part-of-an-inactive-program?code_type=2

# Import your libraries
import pandas as pd

# Start writing code
inactive_program = los_angeles_restaurant_health_inspections[
    los_angeles_restaurant_health_inspections['program_status'] == 'INACTIVE'
]

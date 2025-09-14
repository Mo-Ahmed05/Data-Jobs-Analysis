import numpy as np
import pandas as pd
import ast
from datasets import load_dataset

# Loading... Data
dataset = load_dataset('lukebarousse/data_jobs')
DF = dataset['train'].to_pandas()

# Cleaning the date column
DF["job_posted_date"] = pd.to_datetime(DF["job_posted_date"])

# Converting jobs skills list from string datatype --> list datatype
DF['job_skills'] = DF['job_skills'].apply(lambda x: ast.literal_eval(x) if type(x)==str else np.nan)


# To Convert (Salary Hour Avg) to (Salary Year Avg)
# hours_per_week = 40
# weeks_per_year = 52

DF['yearly_salary_avg'] = DF['salary_year_avg'].fillna(DF['salary_hour_avg'] * 40 * 52)

# DF = DF[(DF['yearly_salary_avg'].notna()) & 
#         (DF['job_title_short'].isin(['Data Analyst', 'Data Scientist', 'Data Engineer']))]
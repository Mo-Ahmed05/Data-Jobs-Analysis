import numpy as np
import pandas as pd
import ast
from datasets import load_dataset

# Loading... Data
dataset = load_dataset('lukebarousse/data_jobs')
jobs_data = dataset['train'].to_pandas()

# Cleaning the date column
jobs_data["job_posted_date"] = pd.to_datetime(jobs_data["job_posted_date"])

# Converting jobs skills list from string datatype --> list datatype
jobs_data['job_skills'] = jobs_data['job_skills'].apply(lambda x: ast.literal_eval(x) if type(x)==str else np.nan)


# To Convert (Salary Hour Avg) to (Salary Year Avg)
# hours_per_week = 40
# weeks_per_year = 52

jobs_data['yearly_salary_avg'] = jobs_data['salary_year_avg'].fillna(jobs_data['salary_hour_avg'] * 40 * 52)
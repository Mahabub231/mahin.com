#problem 01
import pandas as pd

df = pd.read_csv("employees_large.csv")

avg_salary = df.groupby("Department")["Salary"].mean().reset_index()

top_department = avg_salary.loc[avg_salary["Salary"].idxmax(), "Department"]


print(avg_salary)
print("Top Department:", top_department)


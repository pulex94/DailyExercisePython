import pandas as pd

df = pd.read_csv("employees.csv")

salary = df[df["salary"] > 45000]
print(salary)
engineering = df[df["department"] == "Engineering"]
print(engineering)
performance_salary = df[(df["salary"] > 50000) & (df["performance"] == "excellent")]
print(performance_salary)
experience = df[df["years_experience"] < 3]
print(experience)
salary_descending = df.sort_values("salary", ascending=False)
print(salary_descending)
name_department_salary = df[["name", "department", "salary"]]
print(name_department_salary)
print(
    f"Summary of the table:\nMost salary = {salary_descending.iloc[0]["name"]} with: {salary_descending.iloc[0]["salary"]}\nWorst salary = {salary_descending.iloc[-1]["name"]} with: {salary_descending.iloc[-1]["salary"]}"
)
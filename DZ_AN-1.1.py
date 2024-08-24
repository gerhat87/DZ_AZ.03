import pandas as pd
df = pd.read_csv('dz.csv')
avg_salary_by_city = df.groupby('City')['Salary'].mean().reset_index()

# Переименование столбцов для удобства
avg_salary_by_city.columns = ['City', 'Average Salary']
print(avg_salary_by_city)
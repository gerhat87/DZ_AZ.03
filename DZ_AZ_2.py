import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = {
    'students': ['Ni', 'Si', 'Li', 'Ki', 'Lu', 'Re', 'Ben', 'Net', 'Ket', 'Reni'],
    'math' : np.random.randint(1,6, size =10),
    'english': np.random.randint(1, 6, size=10),
    'social science': np.random.randint(1, 6, size=10),
    'history': np.random.randint(1, 6, size=10),
    'biology': np.random.randint(1, 6, size=10)
}
df = pd.DataFrame(data)
print(df.head())
print(f'Средний балл по математике : {df['math'].mean()}')
print(f'Средний балл по английскому языку : {df['english'].mean()}')
print(f'Средний балл по обществозанию : {df['social science'].mean()}')
print(f'Средний балл по истории : {df['history'].mean()}')
print(f'Средний балл по биологии : {df['biology'].mean()}')

print(f'Медианная оценка по математике : {df['math'].median()}')
print(f'Медианная оценка по английскому языку : {df['english'].median()}')
print(f'Медианная оценка по истории : {df['history'].median()}')
print(f'Медианная оценкапо обществозанию : {df['social science'].median()}')
print(f'Медианная оценка по биологии : {df['biology'].median()}')

Q1_math =df['math'].quantile(0.25)
Q3_math = df['math'].quantile(0.75)

IQR = Q3_math - Q1_math

downside = Q1_math - 1.5 * IQR
upside = Q3_math + 1.5 * IQR

df_new = df[(df['math'] >= downside) & (df['math'] <= upside)]


print(f"Стандартное отклонение по математике : {df['math'].std()}")

df_new.boxplot(column = 'math')
plt.show()
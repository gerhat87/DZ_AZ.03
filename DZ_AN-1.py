import pandas as pd
df = pd.read_csv('MentalHealthSurvey.csv')
print(df.head(5))
print(df.info())
print(df.describe())
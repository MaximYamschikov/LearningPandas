import pandas as pd
import numpy as np

df = pd.read_csv(r'c:\ML\LearningPandas\Module\user (2).csv')
dft = pd.read_csv(r'c:\ML\LearningPandas\Module\temperature.csv')
dfc = pd.read_csv(r'c:\ML\LearningPandas\Module\courses.csv')

print(df.sample(n=100,random_state=42)['grade'].sum())
print(dft.ffill()['temperature'].mean().round(2))

# print(dfc.assign(courses = dfc['courses'].str.split(', ')))

a = dfc.assign(courses = dfc['courses'].str.split(', ')).explode('courses').value_counts('courses',ascending=False)
print(a)

# print(dfc['courses'].str.split(', '))
dfc['courses'] = dfc['courses'].str.split(', ')
a = dfc.explode('courses')
print(type(a))
# print(dfc.explode('courses').value_counts('courses',ascending=False).head(1))
# print(dfc.explode('courses').value_counts('courses',ascending=False))
#




# split, explode
# и
# value_counts
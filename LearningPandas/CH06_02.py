from itertools import count

import pandas as pd
import numpy as np




def agg_f(input):
    return input.max() - input.min()


user = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'birthday': ['13.02.2012', '27.12.2008',  '11.08.2005', '13.02.2012'],
    'gender': ['М' , 'Ж' , 'М' , 'Ж'],
    'age': [10, 20, 30, 40],
    })

course = pd.read_csv(r'c:\ML\LearningPandas\Module\course.csv')
user_course_progress = pd.read_csv(r'c:\ML\LearningPandas\Module\user_course_progress.csv')

a = course.merge(user_course_progress,left_on='id', right_on='course_id').dropna()
a['relative_progress'] = a['progress'] / a['max_score']

print(a.agg({'relative_progress':'mean'}).iloc[0].round(2))
print((a['relative_progress'] >= 0.8).sum() )

a = a[a['relative_progress'] >= 0.8]
# print(a)
print(a.groupby('subject', as_index= False).agg({'id':'count'}).sort_values('id',ascending = False).iloc[0])


# course_age = user.groupby('gender', as_index=False).agg({'age': agg_f})
# course_age = user.groupby('gender', as_index=False).agg({'age': lambda x: x.max() - x.min()})
# print(course_age)

# course_age = user_course.merge(user, left_on='user_id', right_on='id')

# print(course_age)
# print(course_age.iloc[1])

#
# print(user.groupby('region', as_index=False) \
#     .agg({'gender': 'nunique'}) \
#     .sort_values('gender'))

# print(user[user['gender'] == 'М'] \
#     .merge(user_course_progress, left_on='id', right_on='user_id') \
#     .groupby('course_id', as_index=False) \
#     .agg({'progress': 'count'}) \
#     .sort_values('progress', ascending=False))
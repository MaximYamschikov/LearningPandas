import pandas as pd
import seaborn as sns

course = pd.read_csv(r'c:\ML\LearningPandas\Module\course.csv')
progress = pd.read_csv(r'c:\ML\LearningPandas\Module\user_course_progress.csv ')

print(progress.groupby('course_id').agg({'course_id':'count'}))

#
# user_subject_progress = pd.read_csv('user_subject_progress.csv')
#
# sns.scatterplot(x=user_subject_progress['math_progress'],
#                 y=user_subject_progress['info_progress'])
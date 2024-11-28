import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
user = pd.read_csv(r'c:\ML\LearningPandas\Module\user_statistics.csv')
user['age_bin'] = pd.cut(user['age'],[0,20,35,float('inf')], include_lowest=True, labels=['0–20', '20–35', '> 35'])
user['avg_session_time_bin'] = pd.cut(user['avg_session_time'],[0,10,40,float('inf')], include_lowest=True, labels=['0–10', '10–40', '> 40'])
data = user.groupby(['avg_session_time_bin','age_bin'], as_index=False).agg({'age':'count'})\
    .rename(columns={'age':'count'}).pivot(index='age_bin', columns='avg_session_time_bin', values='count' ).sort_index(ascending = False)
print(data)
sns.heatmap(data, annot=True, fmt='g',
            cmap=sns.diverging_palette(220, 10, as_cmap=True))
# sns.histplot(user['age'])
# sns.histplot(user['avg_session_time'])
# sns.histplot(user['avg_tries_cnt'], bins=100)
# sns.histplot(user['avg_progress'])
# sns.boxplot(x=user['age'])
plt.show()
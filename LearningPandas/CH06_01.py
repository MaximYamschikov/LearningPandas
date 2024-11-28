import pandas as pd
import numpy as np

def agg_f(input):
    return input.max() - input.min()


df = pd.read_csv(r'c:\ML\LearningPandas\Data\sp500.csv',index_col='Symbol', usecols=[0,2,4,7])

# df = pd.read_csv(r'c:\ML\LearningPandas\Data\sp500.csv', index_col='EBITDA')
s = pd.Series(np.arange(5,25,2))
user = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'birthday': ['13.02.2012', '27.12.2008',  '11.08.2005', '13.02.2012'],
    'gender': ['М' , 'Ж' , 'М' , 'Ж']
    })
# user = pd.read_csv(r'c:\ML\LearningPandas\Module\user.csv', encoding='cp1251', delimiter=';')
# user = pd.read_csv(r'c:\ML\LearningPandas\Module\user.txt', delimiter='\t')
# user_course_progress = pd.read_csv(r'c:\ML\LearningPandas\Module\user_course_progress.txt', delimiter='\t')

# df = pd.read_csv(r'c:\ML\LearningPandas\Data\sp500.csv',index_col='Symbol')
#
# Index(['Symbol', 'Name', 'Sector', 'Price', 'Dividend Yield', 'Price/Earnings',
#        'Earnings/Share', 'Book Value', '52 week low', '52 week high',
#        'Market Cap', 'EBITDA', 'Price/Sales', 'Price/Book', 'SEC Filings'],
#       dtype='object')


# 'Symbol', 'Sector', 'Dividend Yield', 'Book Value'
# c = df.columns
# print(c)
# for i, v in enumerate(c):
#     print(i, v)
# print(df)


course_age = user.groupby('gender', as_index=False).agg({'id': 'agg_f'})
course_age = user.groupby('gender', as_index=False).agg({'id': lambda x: x.max() - x.min()})
print(course_age)

# subject_mean_age = course_age.groupby('subject', as_index=False)
print(user)
# print(user_course_progress)

from traceback import print_tb

import pandas as pd
import numpy as np
import math

user = pd.read_csv(r'c:\ML\LearningPandas\Module\user (3).csv')
user_session = pd.read_csv(r'c:\ML\LearningPandas\Module\user_session.csv')
print(user.columns)
print(user_session.columns)
user['last_visited'] = user['last_visited'].astype("datetime64[ns]")
user['last_visited_m'] = user['last_visited'].dt.to_period('M').dt.to_timestamp()
user_session['date'] = user_session['date'].astype("datetime64[ns]")
user_session['date_m'] = user_session['date'].dt.to_period('M').dt.to_timestamp()


print(sum(user['gender'] == 'М')/len(user))
print(round(sum(user['gender'] == 'М')/len(user),2))

# num = 1.925
# num = 1.425
# num = 2.675
# rounded_num = math.ceil(num)
# print(rounded_num)  # Output: 1.93

# print(round(len(user.query('region == "Краснодарский край" and last_visited_m == "2023-10"')) \
#       /  len(user.query('region == "Краснодарский край"')) ,2) )
#
#
#
# print(round(len(user.query('region == "Краснодарский край" and last_visited_m == "2023-10"')) \
#       /  len(user.query('region == "Краснодарский край"')) ,2) )

# print(user_session[user_session['date_m'] ==  pd.to_datetime('2023-05-01')].groupby('user_id').agg({'session_id':'count'}))
print(round(len(user_session[user_session['date_m'] ==  pd.to_datetime('2023-05-01')].groupby('user_id')) \
            / len(user)
            , 2)
      )


print(round(len(user_session[user_session['date_m'] ==  pd.to_datetime('2023-03-01')].groupby('user_id').agg({'time_watched':'sum'}).query('time_watched >= 60') ) \
            / len(user_session[user_session['date_m'] ==  pd.to_datetime('2023-03-01')].groupby('user_id'))
            , 2)
      )



# print(user['last_visited'].dt.to_period('M').dt.to_timestamp())
# print((user['last_visited_m'] == pd.to_datetime('2023-09-01')) & ())
# date = pd.to_datetime('2018-08-25')
# date = date.to_period('M')
# print(type(date))
# date = pd.to_datetime('2018-08-25')
# date = date - pd.offsets.MonthBegin(0)
# print(date)

from operator import index


import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt


df = pd.read_csv(r'c:\ML\LearningPandas\Data\goog.csv', parse_dates=['Date'])
# print(df[0:1])
# df = pd.read_csv(r'c:\ML\LearningPandas\Data\goog.csv', parse_dates=['Date'], index_col=['Date'])
# print(df.columns)
# print(type(df.Date.[0]))
dates = pd.date_range('2010-01-01','2010-01-05')

temps1 = pd.Series([80,82,85,90,83], index = dates )
temps2 = pd.Series([78,175,69,79,77], index = [-1,3,40,50,9])
# temps2 = pd.Series([78,175,69,79,77])


# print(temps1['2010-01-01'])
# print(temps1[['2010-01-01']])
# print(temps1[['2010-01-01', '2010-01-02']])
# print()
# print(temps1[0:1])
# # print(temps1[[0,1]])
# print(temps1.iloc[[0,1]])
# print(temps2[[0,1,9]])
# print(type(temps2.values))
print(temps2.loc[40:50])
print(temps2.iloc[2]) ##!!!!
print(temps2.iloc[3]) ##!!!!
print(temps2.iloc[2:4]) ##!!!!
# print(temps1[0:1])



# print(type(df.Date[0]))
# print(df.index)
# print(df.columns)
# print(df[df.Date == '2017-03-16'])
# df.Close.plot()
# plt.show()

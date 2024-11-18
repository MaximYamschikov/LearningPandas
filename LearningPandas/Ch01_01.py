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
temps2 = pd.Series([78,175,69,79,77])


print(temps1['2010-01-01'])
# print(type(df.Date[0]))
# print(df.index)
# print(df.columns)
# print(df[df.Date == '2017-03-16'])
# df.Close.plot()
# plt.show()

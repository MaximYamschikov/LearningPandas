from operator import index

import pandas as pd
import numpy as np
from pandas import DataFrame, Series, date_range

# a = pd.Series([5,6,7,8])
# b = pd.Series([5,6,7,8], index = ['a','b','c', 'd'])
# c = pd.date_range('01.01.2010','10.01.2010')
# e = pd.date_range('2010-04-01','2010-04-06')

ind = pd.date_range('2010-01-01','2010-01-10')
# s1 = pd.Series([5,26,27,28,29,210,211,122,213,214], index = ind)
# s2 = pd.Series([1,16,71,18,91,101,111,112,131,114], index = ind)
s1 = pd.Series([5,26,27,28,29,210,211,122,213,214])
s2 = pd.Series([1,16,71,18,91,101,111,112,131,114])

k1 = pd.Series([5,26,27,28,29,210,211,122,213,214])
k2 = pd.Series([1,16,71,18,91,101,111,112,131,114])
k3 = k1 - k2

# print(k1- k2)


dates = pd.date_range('2010-01-01','2010-01-05')
dates2 = pd.date_range('2010-01-01','2010-01-10')
print(dates2)
dates3 = pd.date_range('2010-01-06','2010-01-15')
# dates2.append('2010-03-01')

temps1 = pd.Series([80,82,85,90,83], index = dates )
temps2 = pd.Series([78,175,69,79,77] )

# temps3 = pd.Series([80,182,85,90,83,1,1,1,1,1, 80], index = dates2 )
# temps4 = pd.Series([78,175,69,79,77,2,2,2,2,2, 75] , index = dates3 )

diff_temp = temps1 - temps2
# diff_temp2 = temps3 - temps4
print(diff_temp)
# print(temps3 - temps4)

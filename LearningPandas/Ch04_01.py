
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

ind0 = ['a','b','c','d','e']
ind = ['col1', 'col2', 'col3', 'col4']
temp_msk = [20,15]
temp_spb = [16,18]
t = {'msk':temp_msk,
     'spb':temp_spb
     }

s = pd.Series(ind)

# df = pd.DataFrame(np.arange(1,6), ind)
# df = pd.DataFrame([[1,2,33], [3,4,44]], columns=['col1', 'col2', 'col3'])
# df = df.reindex(ind)
df = pd.DataFrame(t)
df = pd.DataFrame([temp_msk, temp_spb], columns=['msk', 'spb'])
# print(df)


sp500 = pd.read_csv(r'c:\ML\LearningPandas\Data\sp500.csv',index_col=['Symbol'], usecols=[0,2,3,7])
# sp500['Name'] = sp500['Name'].str.lower()
# print(sp500.at['ABBV','Price'])
# print(sp500.Price['ABBV'])
# print(sp500.iat[2,1])
# data.columns = map(str.lower, data.columns)
# or
# data.columns = [x.lower() for x in data.columns]

# print(len(df))
# s[4] = 'col4'
# print(s)
# print(s.index)
# # s.concat
# print(s)

# x = pd.Series()
# N = 4
# for i in range(N):
#    x = x.set_value(i, i**2)
# print(x)

print((333*2222*11111) )
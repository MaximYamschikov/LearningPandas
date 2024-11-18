from operator import index

import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

s = pd.Series(np.arange(100, 110), index = np.arange(10, 20))

ind = ['a','b','c','d','e']
ind = [100, 101, 102,103, 104]
t = pd.Series([10,11,12,13, 14])
# t = pd.Series([10,11,12,13, 14], ind)
# print(s[0:2])
# print(s.loc[10:12])
# print(s)
# print()
# print(s[4::])
# print()
# print(s[-4:-3])
# print(s[(s > 105) & (s < 108)])
# print((s > 105).sum())
# print(s[(s > 105) & (s < 108)])
# print(s[(s > 105) & (s < 108)].count())
t.index = ind
print(t.iloc[].index)

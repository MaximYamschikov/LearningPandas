import pandas as pd
import numpy as np

df = pd.DataFrame({'population': [59000000, 65000000, 434000,
                                  434000, 434000, 337000, 11300,
                                  11300, 11300],
                   'GDP': [1937894, 2583560 , 12011, 4520, 12128,
                           17036, 182, 38, 311],
                   'alpha-2': ["IT", "FR", "MT", "MV", "BN",
                               "IS", "NR", "TV", "AI"]},
                  index=["Italy", "France", "Malta",
                         "Maldives", "Brunei", "Iceland",
                         "Nauru", "Tuvalu", "Anguilla"])
# print(df['GDP'][0])
#print(df.columns[1])
#print(df[df.columns]['Italy'])
#TypeError: Column 'alpha-2' has dtype object, cannot use method 'nlargest' with this dtype
# print(df.nlargest(3, 'alpha-2'))

#return N rows
# print(df.sort_values('alpha-2', ascending=False).head(3))
# print(df.index)

s = pd.Series([1,2,3,5],['one','two','three','five'])

# Pandas Выдает предупреждения:
#FutureWarning: Series.__getitem__ treating keys as positions is deprecated. In a future version, integer keys will always be treated as labels (consistent with DataFrame behavior). To access a value by position, use `ser.iloc[pos]`
s = pd.Series([1,2,3,5],['one','two','three','five'])
print(s[3])

s = pd.Series([1,2,3,5],[3,5,6,7])
# s = pd.Series([1,2,3,5])
print(s[3])


df = pd.DataFrame({
                    'id':  [ 1,  2,  3,  4],
                    'age': [10, 11, 12, 13]},
                    index=['user1', 2 , 3, 'user4']
                 )
# print(df.loc[2,'age'])
# print(df[2])


bl = [
 [10, 'a'],
 [20, 'b'],
 [30, 'c']
]
df = pd.DataFrame(bl)

# print(df)
# print(df.loc[2,1])

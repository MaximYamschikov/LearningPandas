from operator import index

import pandas as pd
import numpy as np


def filter_group_aggregate_sort_solution(df, column_to_filter, filter_set, column_to_group, column_to_aggregate):
    pass


# Дан DataFrame df с ĸолонĸами id, age, city и индеĸсом user1, user2, user3, user4, user5.
# Соотнесите описаниям операции все выражения, выполняющие эту операцию.
df  = pd.DataFrame({
        'id':[1,2,3,4,5],
        'age':[10,20,30,40,50],
        'city':['city101','city102','city103','city104','city105'],
    },
    index = ['user1','user2','user3','user4','user5'])
# print(df)
#Обратиться ĸ ĸолонĸе city.

# print(df['city'])
# print(df[['id', 'age']][['user1', 'user2', 'user3']])
# print(df[['id','age']]['user1':'user3'])
# print(df[['id','age']][ ['user1', 'user2', 'user3']  ])
df = df.assign(test = [1,1,2,2,3])
# print(df.assign(test = lambda df: df['test'] + 10).drop(columns='age').rename(columns={'test':'test2'}))
# print(df.assign(n = lambda df: df['test'] + 10).drop(columns='age').rename(columns={'test':'test2'}))
column_to_filter = 'id'
filter_set = [2,3,4]
column_to_group = 'test'
column_to_aggregate = 'id'
# print(df.query(f'{column_to_filter}.isin(@filter_set)').groupby(column_to_group, as_index=False).agg({column_to_aggregate:'sum'}).sort_values(by = column_to_aggregate, ascending=False))
index_column = 'id'
columns_column = 'age'
values_column = 'test'
print(df.pivot(columns=columns_column,index=index_column, values=values_column).sort_index(axis=0).sort_index(axis=1))
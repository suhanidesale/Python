import numpy as np
import pandas as pd
import csv

# movies = pd.read_csv('movies.csv')
# movies2 = pd.read_csv('movieid.csv')
# print("Movies\n ",movies.head())
# print("MoviesId\n ",movies2.head())

# merged_data = movies.merge(movies2,on=["Security Code"])
# print(merged_data)

df = pd.concat(
    map(pd.read_csv, ['movies.csv','movieid.csv' ]),  axis = 1)
print(df)

df1 = pd.DataFrame({'lkey': ['foo', 'bar', 'baz', 'foo'],
                    'value': [1, 2, 3, 5]})
df2 = pd.DataFrame({'rkey': ['foo', 'bar', 'baz', 'foo'],
                    'value': [5, 6, 7, 8]})

print(df1.merge(df2, left_on='lkey', right_on='rkey'))

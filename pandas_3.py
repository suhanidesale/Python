import numpy as np
import pandas as pd

import pandas as pd

boxes = {'Color': ['Green','Blue','Red'],
         'Shape': [6,10,13]
        }
df = pd.DataFrame(boxes , columns = ['Color', 'Shape'])

print(df)

# df_duplicates_removed = df.drop_duplicates(subset=['Shape'])
# print(df_duplicates_removed)

# print(df['Shape'].value_counts(dropna = False)) #na remove or not
# print(df.notnull())
print(df.describe())
print(df.mean(numeric_only = True))

data = pd.read_excel('SE_IT_GitHubAccounts_python.xlsx')

print(data)

data1 = data.to_excel

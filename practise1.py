import numpy as np
import pandas as pd

dates = pd.date_range("20130101" , periods=6)

print(dates)

df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))

df2 = pd.DataFrame([1,2,3] , [4,5,6])

print("DF1\n" ,df)
print("DF2\n" ,df2)

pd.merge(df,df2)
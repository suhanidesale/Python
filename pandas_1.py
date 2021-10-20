import numpy as np
import pandas as pd
import csv

dict1 = {
    "name" : ["suhani" , "mayuresh" , "om"],
    "mark" : [12 , 34 , 25],
    "city" : ["Kalyan" , "Bandra" , "Dadar"]
}
df = pd.DataFrame(dict1)
df.to_csv('family.csv')

members = csv.reader(open("family.csv","rU"))
for row in members:
 for index in (1, 0):
   if index < len(row):
      print (row[index])


for x in df.index(6):
  

# for index, row in df.iterrows():
#     print(row)

 print(df)

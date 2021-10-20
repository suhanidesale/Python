import numpy as np;
import pandas as pd;
ser = pd.Series(np.random.rand(34))

#print(type(ser))

newdf = pd.DataFrame(np.random.rand(50,2) , index = np.arange(50))
# print(newdf)

#print(newdf.sort_index(axis = 0 , ascending= False))
# print(newdf)\

newdf2 = newdf #new def 2 is a view of newdf 2
newdf2 = newdf[:] # or .copy is copy of newdf

newdf2.loc[0][0] = 45 #we should set the valuse using loc 
#print(newdf2)

# def loop():
#  i = 1
#  #while i < len(newdf):
#  for v in range(len(newdf)):
#    print(i)
#    i = i+ 1

#newdf.columns = list('CD')
#print(newdf)

#print(newdf.loc[[1,2] , [1]])

# print(newdf.loc[(newdf[1] < 0.3)])

# newdf.iloc[0,1] ##to display the particular element


print(newdf.drop([0])) #for permanently use implace or =


print(newdf.reset_index(drop = True , inplace = True)) #inplace does for real

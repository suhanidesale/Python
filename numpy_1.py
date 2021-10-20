import numpy as np;
li = [2,3,4,5]
n1 = np.array(li)
print(n1)

n2 = np.zeros((1,2))
print(n2)

n3 = np.full((2,2),3)
print(n3)

n4 = np.arange(50,61)
print(n4)

n5 = np.arange(50,100,5)
print(n5) 

n6 = np.random.randint(12,20,4)
print("n6",n6)

n7 = np.array([[2,3,4,5],[6,7,8,9]])
n7.shape = (4,2)
print(n7)

n8 = np.array([[1,25,8] , [8,1,2]])
n9 = np.array([8,9,10])

n10 = np.array([[2,3,4],[6,7,8],[4,5,6]])
print("SUM",n10.sum(axis=0)) # AXIS -0 for column and 1 for rows
print(np.vstack((n8,n10)))

ans = (n10.transpose())
print("dot\n",ans)  
# print(dir(np))

n11 = np.sort(n10 , axis = 0)
n12 = np.sort(n10 , axis = 1)
print("0 ",n11," \n","1 ",n12) 


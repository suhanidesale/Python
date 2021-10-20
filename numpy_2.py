import numpy as np;
n1 = np.array([10,20,30])
n2 = np.array([10,40,50])
n3 = np.intersect1d(n1,n2)
print(n3)

n4 = np.sum([n1,n2])
print(n4)
n5 = np.sum([n1,n2] , axis = 0)
print(n5)
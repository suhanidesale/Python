import numpy as np;
n1 = np.array([10 , 20 , 30])
n1 = n1+1
print(n1)

n2 = np.random.randint(1,20,7)
print(n2)
n4 = np.median(n2)
print(n4)
n5 = np.mean(n2)
print(n5)
n6 = np.std(n2)
print(n6)


np.save('numpy_3' ,n1)
n6 = np.load('numpy_3.npy') #to load saved array
print(n6)

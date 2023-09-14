#add two array in single list and add two array element in single list
import numpy as np
arr1=np.array([1,2,4,5,6])
arr2=np.array([7,8,9,10,11])
add=arr1+arr2
arr3=np.concatenate((arr1,arr2))
print(arr3)
print(add)




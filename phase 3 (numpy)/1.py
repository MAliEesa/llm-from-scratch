"""numpy is python library to do math oprations we import numpy then here we 
used np.array meaning its creating an array but its differnt from normal 
python lists pythons lists are slow for math opration numpy array are very fast 
for it normal list can hold different types of elements int string bool typle
dict in a single list but numpy array will onyl have smae elements normal list
stores refrences to objects while numpy arrrays stores data into contagious 
memory normal list not good for vector math need loops lots of loops numpy
array supports it so no loop need directly arr*2 will work list size can change
numpy array size is fixed numpy array has fucnitons that can be used sum dot 
mean"""
import numpy as np
arr1 = np.array([1,2,3,4,5])
arr2 = np.array([[1,2,3],[4,5,6]])
arr3 = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])

for i in arr1:
    print(i)

for j in arr2:
    print(j)
for k in arr3:
    print(k)

print(arr1)
print(arr2)
print(arr3)
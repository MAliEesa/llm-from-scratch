"""reshape change the shape (rows*columns*dimensions) it has one rule all 
elements should result total number of elements now we had arr1 of 12 elemenets
first we had written np.reshape(arr1,-1) -1 tells python to automaticlaly figure 
it out while in next one written (3,4) mreaning create 3 rows and 4 columns
now 3*4 = 12 so total element was 12 so it spossible but if we try (6,7) 
6*7 = 42 total element = 12 so not equal it will give error"""
import numpy as np
arr1 = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print(np.reshape(arr1,-1))
print(np.reshape(arr1,(3,4)))
print(np.reshape(arr1,(4,3)))
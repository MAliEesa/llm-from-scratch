""""@ is used for matrix multipication it has one rule first ones columns
must be equal to the the next matrix arrays if this condition not fuillfilled
you will get error"""
import numpy as np
arr1 = np.array([[1,2,3],[4,5,6]])
arr2 = np.array([[7,8,9],[10,11,12],[13,14,15]])
print(arr1@arr2)

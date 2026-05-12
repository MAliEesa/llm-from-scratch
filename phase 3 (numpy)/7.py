"""max() gives us max number, min gives us minimum number ,mean give us its
mean difference between two , and sum gives us its sum ther is one more .
maximum it gives us the compares 2 arrays make one new array of and then '
return its larger values"""
import numpy as np
arr = np.random.randint(1,1000,(1,10))
print(np.min(arr))
print(np.max(arr))
print(np.mean(arr))
print(np.sum(arr))
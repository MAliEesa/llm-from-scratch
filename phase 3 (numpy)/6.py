"""np.random.rand() purpose to generate a random matrix having float number 
from 0 to 1 inside  we write diemnsion rows and colums of it then 
np.random.randint() its lets us create a randome matrix it take
(starting number , ending number , (diemnsions of matrix)) anmd generate 
a random matrix for us

"""
import numpy as np
print(np.random.rand(3,3))
print(np.random.randint(1,1000,(3,3)))
print(np.random.randint(1,1000,(1,10)))

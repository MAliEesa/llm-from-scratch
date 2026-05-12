"""here we all calculating loss function basically ther are thee kind of loss 
functions are
1 MSE mean sqaured error we used this one here 
2 MAE mean absolute function
3 class entropy used in LLMS
now mean squared is very simple you need to subtract our gotten output from 
forward pass meaning the final output of our multilayer neural network that 
output be subtracted from actual values now actual value is the vlaue that we 
desired actually and then whole power of it 2 then mean of th ewhole thing """
import numpy as np
pridictions = np.array([2,4,6,8])
actual_values = np.array([1,3,5,7])
error = (pridictions-actual_values)**2 # finding square of it 
print(np.mean(error))# mean of it now so it bcoems mean squared error is printing
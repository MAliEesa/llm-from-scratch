"""now to make a neuron in python first understnad what a neuron actually is 
a neuron is simply a has inputs weights and output now how it works to create a
neuron we mulpitply inputs with weights weights always put first then 
add bias so to stable it if input like or weight 0 cuase at first we take 
ás random so muplityping it bcoems 0 it wil effect output so bias added to 
stable it now comes her ein this one we used relu function is very basic
if weighht*inputs + bias < 0  relue will give no output or zero neuron not
firing but if greator then zero or equal zero then the neruon will fire output 
here we did dot [product because only cause numpy array was only one dimensional
array of numpy if in matrix fomr then use @ for matrix mulitplciation ]"""
import numpy as np
def ReLu(inputs,bias,weights):
    output = np.dot(inputs,weights) + bias
    if output < 0:
        output = 0
        return output
    else :
        return output
inputs = np.random.randint(1,100,3)
weights = np.random.randint(1,1000,3)
bias = 0.1
print(ReLu(inputs,bias,weights))


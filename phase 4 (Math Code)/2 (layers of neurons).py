import numpy as np
def layer1(inputs,weights,bias):
    neurons = weights @ inputs + bias # simple matrix mulitpication 
    output = neurons
    return np.maximum(0,output) 
    """maxiumum compares both thigns an dgive the lareger one so we are 
    using this stratigically to get use of ReLU"""
    
inputs = np.random.randint(1,10,4)
weights = np.random.randint(1,10,(3,4))
bias = np.random.randint(1,10,3)
print(layer1(inputs,weights,bias))



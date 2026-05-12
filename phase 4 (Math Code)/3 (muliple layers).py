""""now here we are using multillayered menaing one neuron output going into
the next neuron same its output clacualted with funciton goin inbto next one 
till the last one now so bascialy we can say we had 4 inputs we had  2 
hidden layer then final output layer """
import numpy as np
def layers(inputs,weights,bias): # relu function to use it on all wihtout 
    neurons = weights @ inputs + bias # writingn again 
    output = neurons
    return np.maximum(0,output)
    
inputs = np.random.randint(1,10,4)
weights = np.random.randint(1,10,(3,4))
bias = np.random.randint(1,10,3)
output1 = layers(inputs,weights,bias)

"now layer 2"

weights = np.random.randint(1,100,(4,3))
bias = np.random.randint(1,1000,4)
output2 = layers(output1,weights,bias)

"now layer 3"

weights = np.random.randint(1,100,(2,4))
bias = np.random.randint(1,1000,2)
output3 = layers(output2,weights,bias)
print(output3)

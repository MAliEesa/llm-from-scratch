"""same traning loop but now done in aloop so it can repeat"""
def output(weight,inputs,bias):
    output = (weight*inputs)+bias
    return output

def loss(output,actual):
    loss = (output-actual)**2
    return loss
    
def derivative(output,actual,inputs):
    gradient = 2*(output-actual)*inputs
    return gradient
   

def update(weight,learning_rate,gradient):
    weight = weight - learning_rate * gradient
    return weight

    
inputs = 2.0
weight = 0.5
bias = 0.1
actual = 10.0
learning_rate = 0.01
for i in range(100):
    o = output(weight,inputs,bias)
    l = loss(o,actual)
    print(f"loss is {l}")
    g = derivative(o,actual,inputs)
    weight = update(weight,learning_rate,g)

"""this is our traning loop ity has four parts this is how we train ai
1 Forward pass 
2 Loss calculation 
3 backpropagation 
4 gradient loss 
5 repeat until loss gets lower 
this is how we train ai we give our inputs 
now forward pass means the process form inputs to going to its final output
through layers of neurons but here only one neuron exists so after innput one
neuron and then it goes into the Relu function but here we had not used it 
then do loss calulation is simple use calulated (output-actual)**2 then do its 
mean but here for single neuron we dont need to do the mean but for more neurons 
you may use mean moving to vbackporopagation okay once loss calulated now 
we need to go back gfrom output y to the layers back and then to the input 
so we use chain rule to find the relation of output bakcward to weights thats
backopropagation here we had derived chain rule manually and putted the formula
and it will give us the graident meaning derivative nowe we need to do the 
gradient loss the thing is if in back propagation we got a positive graident'
we need to minus fro our weights but if in back propagation our gradient was 
negative we need to add in our weights thats how we do it and learning rate
is the rate using in gradient if its small small change will happen if too large 
the ai wont learn apttern instead memeoriezs it and fail in new question so 
better to give it small and then finally repeate the process    
inputs result   """
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
output1 = output(weight,inputs,bias)
loss1 = loss(output1,actual)
gradient1 = derivative(output1,actual,inputs)

"updating weights"
newweight = update(weight,learning_rate,gradient1)
weight = newweight
output2 = output(weight,inputs,bias)
loss2 = loss(output2,actual)
gradient= derivative(output2,actual,inputs)
print("loss before:", loss1)
print("loss after:", loss2)
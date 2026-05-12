"""here we are using now torch libray which in python is used for the building
and training of deep neural netwokring 
here we did not do anything new only did this we used t.tensor this tensor 
thing any tuple maded in it like t.tensor[2,3] it will track it actullay
and we can directly use it for purposes  so in more genral sense
a tensor is the fundamental data structure in pytorch it cna hold 
scaler for  0d array or tuple vector 1d array or tuple and matrix 2d or more 
array of vector and for tracking anything we need to make require_grad = True
"""
import torch as t

def output(weight,inputs,bias):
    output = (weight*inputs)+bias
    return output

def loss(output,actual):
    loss = (output-actual)**2
    return loss

"""t.no_grad is a context manager when used with "with" keyword that will close
it automaticlaly and enter in it not its purpose to create a block where
the tracking of the tensor having require_grade = True if not in funcitons
we may get erros like to not let it create anew tensor"""

def update(weight,learning_rate,grad):
    with t.no_grad():
        weight -= learning_rate*grad # formule to update weights 
    return weight

i = t.tensor(2.0) # inputs
w = t.tensor(0.5,requires_grad=True) # weights will be tracked
b = t.tensor(0.1) # bias
a = t.tensor(10.0) # actual value
l = t.tensor(0.01) # learning rate

for j in range (100): # using loop for traning 
    o1 = output(w,i,b) 
    l1 = loss(o1,a)
    print(f"loss is {l1}")
    
    """variable.backward() is a function of torch that automaticlaly calculates
    gradient using chain rule we dont need to manually dervie the formula
    and hard code it torch was already tracking weights  and we need weights
    but we do need the other rvlaues like input output and loss right 
    so it has also a way for it too thing is torch only track requre_grad 
    = True ones but it makes th eother vlaues as constants unchanagble values
    they stil beused in graphsnot remebered """
    
    l1.backward() # it has no return  
    
    """backward() dont return anything instead it just stores it in 
    w.grad you can check this by print(w.grad)"""
    print(w.grad)

    """now for theupdate we actually need our weights our learnigrateand our
    chainrule derivative calulation so aocrinding ot the derviative we can 
    add if derviativ e is negative into weights and minus form it if derivative
    positive so w.grad already holds the backpropgation finded derivative value
    in w.grad so that why it is passed as aparameter """

    w = update(w,l,w.grad) 

    """w.grad.zero() is a torch function that lets you erase all gradients
    grpah calcualtion so the next time we do backprophation calulation 
    through backward() we dont mess it with the old data """

    w.grad.zero_()  
"""torch.nn is pytorch neural network library and torch.optim is torch for
using algorithums for our neural networking both of these lets us automate
things """

import torch as t
import torch.nn as nn
import torch.optim as o

"class for t.module"
class N(nn.Module):
    def __init__(self):
        super().__init__()
        self.H1 = nn.Linear(3,8)
        self.H2 = nn.Linear(8,4)
        self.F  = nn.Linear(4,1)
        self.R = nn.ReLU()

    def forward(self,inp):
        inp = self.H1(inp)
        inp = self.R(inp)
        inp = self.H2(inp)
        inp = self.R(inp)
        inp = self.F(inp)
        return inp


"Data set"
x = t.tensor([[1.0,2.0,3.0],[4.0,5.0,6.0],[7.0,8.0,9.0],[2.0,4.0,6.0]])
y = t.tensor([[6.0],[15.0],[24.0],[12.0]])

"Making objects"
M = N()
C = nn.MSELoss()
O = o.Adam(M.parameters(),lr = 0.01)

"Traning loop"
for i in range(5000):
    output = M(x)
    print(output)
    loss = C(output,y)
    if (i+1) % 50 == 0:
        print(f"Epoch {i+1}, loss: {loss}")
    loss.backward()
    O.step()
    O.zero_grad()

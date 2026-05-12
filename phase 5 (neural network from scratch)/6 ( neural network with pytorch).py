
import torch as t
import torch.nn as nn
import torch.optim as optim

class nun(nn.Module):
    def __init__(self):
        super().__init__()
        self.layer1 = nn.Linear(2,4)
        self.Re = nn.ReLU()
        self.layer2 = nn.Linear(4,1)
    
    def forward(self, x):
        x = self.layer1(x)
        x = self.Re(x)
        x = self.layer2(x)
        return x

x = t.tensor([[1.0,2.0],[3.0,4.0],[5.0,6.0]])
y = t.tensor([[3.0],[7.0],[11.0]])

model = nun()
criterion = nn.MSELoss()
optimizer = optim.SGD(model.parameters(), lr=0.01)
for i in range(100):
    f = model(x)
    l = criterion(f,y)
    print(f"lodd id {l}")
    g = l.backward()
    optimizer.step()
    optimizer.zero_grad() 

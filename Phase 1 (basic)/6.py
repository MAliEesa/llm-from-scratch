class new :
    def __init__ (self):
        pass
    
    def work (self,x):
        x += 2
        return x 

inp = int(input())
n = new()
print(n.work(inp))

"""the init thing is called a contructor its purpose to tos tore object values into'
its own attributes but we wil sue the sasme varable"""

class test2:
    def __init__(self,name):
        self.name = name 

    def n(self):
        print(self.name)

x = test2("ali")
x2 = test2("sara")
x.n()
x2.n()

"""we can also do things on its own wihtout any constructor at all but then we need to pass
values in it and if we forget even once we get an error """

class test:
    def name(self,x):
        print( x) 

t1 = test()
t1.name("ali")
t2 = test()
t2.name("sara")


"""Abstraction is used to hide complexity of things in it even the parent
class is inherited from ABC if we make a function in it for example in this
example we had used shape(ABC) our parent class is also inherting from 
ABC menaing abstract base class givnig us abstract methdo now inside we had
written @abstractmethod it stops this class ot have direct instantiation 
meaning to stop it from making its object s = shape() this will not work 
in it we had define a function area but used passed nothing inside then 
subclasses we maded subclass circle and rectangle each with its own 
constructor and and th earea method now well thing is we had one area right 
in main class all inheriting from it having there own area functions this is 
hiding complexty but look at class triangle it also is a subclass inherting
from shape but nothing inside but when we run this program we will get error
why cause each subclass of the parent abstract class must implement the 
method given in the parent class if not then it wil give error its considered 
anotehr abstract class so cant be instantiate until it had thta exact method 
properly ut key detail if you make a method named area but pass in it nothing
it will notbe considered a abstract but instead  a propersubclass then it can
be instantiated   """
from abc import ABC, abstractmethod

class shape(ABC):
    @abstractmethod
    def area(self):
        pass

class circle(shape):
    def __init__(self,radius):
        self._radius=radius

    def area(self):
        area=3.14* self._radius*self._radius
        print(area)

class rectangle (shape):
    def __init__(self,length,width):
        self._length = length
        self._width = width

    def area (self):
        area=self._length*self._width
        print(area)

class triangle(shape): # not gona work its a abstract class still not sub class
    pass # its a new sub abstract class of shape so not gona work 

class  blue (shape): # gona work its a subclass now 
    def area (self):
        pass

cir = circle(2)
cir.area()
rec = rectangle(2,2)
rec.area()
tri = triangle() # not gona work
b = blue () # gone work 


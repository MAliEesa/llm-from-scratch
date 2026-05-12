"""in python there are no private varaible but when we write something with
self.__x = x it wil trigger a phenomena called name mangling it does this
it dont make it private but the orignal varibale cant be directly accesed 
for example 
class n :
    def __init__ (self,x):
        self.x = x 
n = n(2)
print(n.x) this will now work but when we do name mangling we cant
class n :
    def __init__ (self,x):
        self.__x = x 
n = n(2)
print(n.x)this is not gona work but 
print(n._n__x) now this its new name when we did name mangling we can access
it still by this so not private properly 
"""
class students:
    def __init__ (self ,  name, marks):
        self.__name = name
        self.__marks = marks
        
    def setmarks(self,newmarks):
        if newmarks > 100 or newmarks<0 :
            print("invalide marks entered ")
        else :
            self.__marks = newmarks 
        
    def getmarks(self):
        print(f"{self.__name} has marks {self.__marks}")

student_1 = students("ali",123)

student_1.setmarks(23)
student_1.getmarks()
"""älso this is encapsulaiton that we are hding data through name mangling """

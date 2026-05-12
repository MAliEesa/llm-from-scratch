"""Inheritance is one of the keyconcepts of oop its purpose for a child class
to inherit from its parent class the child class will get all of its varaibles
and methods for it know that it inherits variables from parent class we use 
super()"""
class person :
    def __init__(self,name,age):
        self.__name = name
        self.__age = age

    def getname(self):
        return self.__name

    def get(self):
        print(f"{self.getname()} is {self.__age} years old")

class student(person):
    def __init__ (self,name,age,marks):
        super().__init__(name,age)
        self.__marks=marks

    def addmarks(self,newmarks):
        self.__marks = newmarks
        self.get()
        self.getmarks()
        
    def getmarks(self):
        print(f"{self.getname()} has marks {self.__marks}")

student_1 = student("ali",23,90)
student_1.addmarks(50)
        

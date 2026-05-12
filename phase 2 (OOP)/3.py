"""class is a blue print for something while object is the real world entity
that can interact with class here we had used firstly something called a 
constructor its purpose is to store each object into its attribute wjy its 
usefull cause next time yuou dont need to pass your arguments in class 
class functions it will directly take from the contructor meaning one time
intializing only  """
class student :
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def grab(self):
        print(f"{self.name} has marks {self.marks}")


student_1 = student("ali",90) # self.name and self..age safes it
student_2 = student("sara",95)# same self.name saves it but not mess it wit others
student_3 = student("lala",440)

student_1.grab() # we never passed anything yet its getting fomr constructor 
student_2.grab()
student_3.grab()
"""still its not alaways essential to make a constructor we can do same thing
by passing each function indivial arguments but it has higher chance of error"""
"""polymorphisim is bascially this we have one singe method like speak in animal
but each of them give there own sounds cats mewo dogs bark duck quaks so 
its one method doing many forms and we are accesing all by a single method 
thats polymorphisim """
class animal:
    def speak(self):
        print("speak some osund")

class dog(animal):
    def speak(self):
        print("woof")

class cat(animal):
    def speak(self):
        print("meow")

class duck(animal):
    def speak(self):
        print("quack")

animal_list = [animal(),cat(),dog(),duck()]
for i in animal_list:
    i.speak()

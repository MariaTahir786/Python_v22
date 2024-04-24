from classes.human import Human

class Student(Human):
    def __init__(self , name, age, school):
        super().__init__(name, age )
        self.school=school

    #implementation of abstract methods
    def work(self):
        print(f"{self.name}, the student is studying at{self.school}")

#polymorphism
    def communicate(self,message="Hello",words="text"):
        if words== "text":
            print(f"{self.name},the student ,texts:'{message}'")
        else:
            print(f"{self.name},the student ,says loudly{message}'")
        
    #additional methods
    
    def study(self):
        print(f"{self.name} is studying")

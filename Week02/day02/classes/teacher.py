"""
implementation of abstract method
additional method to teacher
#overload and overload of communicate
create instance of teacher in app.py
test all methods
"""
from classes.human import Human
class Teacher(Human):
    def __init__(self, name ,age, school):
        super().__init__(name,age)
        self.school=school
        
        #implementation of abstract methods
    def work(self):
        print(f"{self.name},the Teacher is taeching at {self.school}")
        
    def communicate(self, message="Hello Students",in_class=False):
        if in_class:
            print(f"{self.name}, the teacher will announce{message}")
        else:
            print(f"{self.name}, the teacher whispers {message}")
            
            #additional methods
    
    def teaching(self):
        print(f"{self.name} is teaching")
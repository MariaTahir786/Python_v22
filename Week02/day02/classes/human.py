#to implement  absration
from abc import ABC,abstractmethod

class Human(ABC):
    population =0
    #constructor
    def __init__(self, name, age):
        self.name=name
        self.age=age
        #whenever student or teacher added it will increment by one
        Human.population +=1
        
        
    # common methods for all==> instance level 
    # eat
    # sleep
    # walk
    # Runt
    # communicate
    
    
    
    def eat(self):
        print(f"{self.name} is eating")
        return True
        
    def sleep(self):
        print(f"{self.name} is sleeping")
        return True
        
    def walk(self):
        print(f"{self.name} is walking")
        return True
        
    def run(self):
        print(f"{self.name} is running")
        return True
        
        
    #communicate methods with optional parameters we are achieving polymorphism here
    
    def communicate(self,message="Hello"):
        print(f"{self.name} says,'{message}'")
        return True
        
        
    #decorator
    @classmethod
    def get_population(cls):
        return f"Total number of human: {cls.population}"
    
    @abstractmethod
    def work(self):
        pass
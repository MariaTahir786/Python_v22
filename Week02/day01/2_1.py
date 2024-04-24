
import random
class Animal: 
    #class level data
    animals = []

    #Constructor
    def __init__(self, name, species, age, energy=100): # instance level data -- all available through instance fo class
        self.name = name
        self.species = species
        self. age = age
        
        self.energy = energy
        Animal.add_animal(self) # it adds new instance to the animals list
        
    
    # Behavior/ Instance Methods
    def sleep(self):
        return f"{self.name} is sleeping!!!"
    
    # overriding
    def make_sound(self):
        print("Making Sound")
    
    def walk(self, distance):
        self.energy -= distance # energy = energy - distance
        return f"{self.name} walked {distance} miles and lost {distance} energy!. {self.name} has now {self.energy} energy level left!!!"

    def eat(self, food_name, energy):
        self.energy += energy # energy = energy + energy
        return f"{self.name} ate {food_name} and gained {energy} energy!. Now, {self.name} has {self.energy} energy level"

    # Create a method for animal description that says " {name} is a {species} and is {age} years old. "
    def get_description(self):
        return f"{self.name} is a {self.species} and {self.age} is years old."
    
    
    @classmethod # decorator
    def pass_time(cls):
        pass

    @classmethod
    def add_animal(cls, animal):
        cls.animals.append(animal)
        
    @staticmethod
    def calculate_distance_between_animals(animal_1, animal_2):
        pass

# kitty = Animal("Kitty", "Cat", 3)
# rover = Animal("Rover", "Dog", 5)
# charlie = Animal(species="Parrot", name="Charlie", age=2, energy=110)

# print(kitty.name)
# print(rover.name)
# print(charlie.name)

# Animal.add_animal(kitty)
# Animal.add_animal(rover)
# Animal.add_animal(charlie)

#Classes
class Dog(Animal):
    #overriding
    def make_sound(self):
        print("Bark")
    #overloading
    def sleep(self, time):
        return f"{self.name} has been sleeping for ${time}!!!"

class Cat(Animal):
    pass

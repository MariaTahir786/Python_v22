# create Animal class

class Animal: 
    
    #Constructor
    def __init__(self, name, species, age, energy=100):
        self.name = name
        self.species = species
        self. age = age
        
        self.energy = energy
        
    
    # Behavior/Methods
    def sleep(self):
        return f"{self.name} is sleeping!!!"

    def walk(self, distance):
        self.energy -= distance # energy = energy - distance
        return f"{self.name} walked {distance} miles and lost {distance} energy!. {self.name} has now {self.energy} energy level left!!!"

    def eat(self, food_name, energy):
        self.energy += energy # energy = energy + energy
        return f"{self.name} ate {food_name} and gained {energy} energy!. Now, {self.name} has {self.energy} energy level"

    # Create a method for animal description that says " {name} is a {species} and is {age} years old. "
    def get_description(self):
        return f"{self.name} is a {self.species} and {self.age} is years old."
    
    
    
kitty_1 = Animal("Kitty", "Cat", 4, energy=90)

dog = Animal(species="Dog", name="Rover", age=8)

# animals = [Animal("Kitty", "Cat", 4, energy=90), Animal("Rover", "Dog", 8)]

#? Access to attribute
# Dictionary --> ['key']

# print(kitty_1.energy)
# print(kitty_1.name)
# print(kitty_1.species)
# print(kitty_1.age)

# print(dog.name)
# print(dog.species)
# print(dog.age)
# print(dog.energy)

#? Access to methods
print(kitty_1.sleep())
print(kitty_1.walk(5))
print(kitty_1.eat("Fish", 15))
print(kitty_1.get_description())

print("### Dog Object ###")
print(dog.sleep())
print(dog.walk(10))
print(dog.eat("Sausage", 20))
print(dog.get_description())

t = 1
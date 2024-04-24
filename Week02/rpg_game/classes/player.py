class Player:
    # dunder method
    def __init__(self, name, strength = 100 ) -> None:
        
        self.name = name
        self.strength = strength
        
#whenever character walk in direction it will gain random weapon which will be stored in this list
        self.weapons = []
        
    def walk(self):
        self.strength-=1
        return self.strength   
    
    def add_weapon(self,weapon):
        self.weapons.append(weapon)
        return weapon 
import random
from classes.food import Food
from classes.player import Player
from classes.weapon import Weapon

player = Player("Fred")

is_playing = True


available_weapons = [
    ("sword", 10, 2),
    ("shield", 4, 6),
    ("chain mail", 0, 4),
    ("axe", 15, 2),
    ("bow", 5, 0),
    ("dagger", 3, 0),
    ("mace", 12, 2),
]

available_foods = [  # TUPLES!
    ("apple", 5),
    ("bread", 10),
    ("ale", 12),
    ("cheese", 8),
]

print(f"Welcome to the game, {player.name}!")
print("Type 'help' for a list of commands.")

# our game loop
while is_playing:

    print(f"\nYour strength is {player.strength}.")
    command = input("Enter a command: ")

    if command == "quit":
        is_playing = False

    elif command == "help":
        print("\nAvailable commands:")
        print("\nquit - quits the game")
        print("help - prints this help message")

    elif command == "walk":
        """ 
        choose a direction 
        distance/speed
        energy reduction
        feedback - "you walked
        """
        direction = input("Which direction? (e, w, n, s): ")
        if direction not in "ewns":
            print("\nYou cannot walk that way!")
            continue
        print("\nYou walk "
            + {
                "e": "East", 
                "w": "West", 
                "n": "North",
                "s": "South"
            }[direction])
        
        if player.walk() == 0:
            print("You died")
        
        roll = random.randint(1, 10)
        
        if roll < 0:
            pass
        
        elif roll < 0:
            pass # challenge food
        
        elif roll < 11: # find a weapon
            #              available_weapons[2]
            weapon_choice = available_weapons[random.randint(0, len(available_weapons) - 1)]
            weapon = player.add_weapon(Weapon(weapon_choice[0], weapon_choice[1], weapon_choice[2]))
            print(f"\nYou found {weapon.name}!")
        else: 
            print("You see a dark void")
    #challenge
    elif command == "list food":
        pass
#challenge
    elif command == "eat":
        # will need a follow up question?
        pass
        
        
print("Thanks for playing!")
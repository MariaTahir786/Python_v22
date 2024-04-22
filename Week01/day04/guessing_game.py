"""
    CLI - Command Line Interface
"""

# input - library

# response = input("\nWhat is your name? ")

# print(f"Hello, {response}")

import random

# print(random.randint(1, 10))
# while loop
is_playing = True

while is_playing:
    print(random.randint(1, 100))
    response = input("\nWhat is your name? ")
    
    if response.lower() == "quit":
        is_playing = False
    else:
        print(f"Hello, {response}")
        
print("Have a nice day")
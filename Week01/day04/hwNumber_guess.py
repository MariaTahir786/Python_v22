
# Requirements:
#         - User enters their guess between (1 to 100)
#         - User is told if their is too high or too low
#             - continue guessing
#         - User is told if they guessed correctly
#             - print total number of guesses
#             - end game
#             - Thank the user for

import random
secret_number=random.randint(1,100)
attempts=0
max_attempts=5
print("Choose a number from 1,100: ")
 
while attempts<max_attempts:
      attempts+=1
      guess=int(input("Make your guess: "))
      
      if guess<1 or guess>100:
        print("Invalid number ,please enter a number between 1,100")
        continue
      if guess>secret_number:
        print("Wrong ,the number you guessed is higher than the secret number, try again")
    
      elif guess<secret_number:
        print("Wrong ,the number you guessed is lower than secret number,try again")
        attempts=attempts+1
      else:
        print(f"Yayyyy!!! you guessed it  secret number  {secret_number} in {attempts} attempts") 
        print("Thank you for playing")
        exit()
print(f"out of attempts! sectret number was {secret_number}")
print("Thank you for playing")
    
    
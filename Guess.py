# Number guessing project

import random 

number_val_1 = int(input("Choose the first range "))
number_val_2 = int(input("Choose the second range "))

number = random.randrange(number_val_1,number_val_2)
print(number)

user_guess = int(input("Guess the number "))

while user_guess != number: 
  if user_guess > number: 
    print("Too high")
    user_guess = int(input("Guess again "))
  else:
    print("Too low")
    user_guess = int(input("Guess again "))

print("You guessed the right number! ")

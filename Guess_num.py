# Imports random library
import random
# The computer chooses a random number between 1 and 100
comp = random.randint(1,101)
# Asks user to guess the number
while True:
    try:
        user = int(input("Guess the number "))
        if user == comp:
            print("You got it!!")
            break
        elif user < comp and user < 50:
            print("Guess a litle higher :)")
        elif user < comp and user > 50:
            print("Guess a lot higher")
        elif user > comp and user > 50:
            print("Guess a litle lower")
        elif user > comp and user > 100:
            print("Please enter a number less than or equal to 100")
        else:
            print("Guess a lot lower :)")
    except ValueError:
        print("You must enter an integer")
   

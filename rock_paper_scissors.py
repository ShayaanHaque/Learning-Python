
#importing random
import random
#asking user for number of rounds
while True:
    try:
        rounds = int(input("How many rounds do you want "))
        break
    except ValueError:
        print("Please enter a number")
for i in range(0,rounds):
    #Asks for users input
    user = input("Choose rock, paper or scissors ").strip()#Removes whitespaces
    # The computer chooses rock,paper,scissors randomly
    comp  = random.choice(["rock","paper","scissors"])
    #Prints users input and the computers random choice
    print(f"You choose {user} and I choose {comp}")
    
    # Defines a score value for the user
    user_score = 0
    # Defines a score value for the computer
    comp_score = 0
    if user == "rock" and comp == "paper":
        print("One point for me")
        comp_score += 1
    elif user == "paper" and comp == "rock":
        print("One point for you")
        user_score += 1
    elif user == "rock" and comp == "scissors":
        print("One point for you")
        user_score += 1
    elif user == "scissors" and comp == "rock":
        print("One point for me")
        comp_score += 1
    elif user == "scissors" and comp == "paper":
        print("One point for you")
        user_score += 1
    elif user == "paper" and comp == "scissors":
        print("One point for me")
        comp_score += 1
    else:
        print("Tie")
if user_score > comp_score:
    print("You won")
elif user_score < comp_score:
    print("You lost")

    
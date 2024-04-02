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
    user = input("Choose rock, paper or scissors ").strip()#Removes whitespace
    # The computer chooses rock,paper,scissors randomly
    comp  = random.choice(["rock","paper","scissors"])
    #Prints users input and the computers random choice
    print(f"You choose {user} and I choose {comp}")
    user_score = 0
    comp_score = 0
    match user:
        case "rock":
            if comp == "paper" :
                print("One point for me ")
                comp_score += 1
            if comp == "scissors" :
                print("One point for you")
                user_score += 1
            if comp == "rock":
                print("Tie")   
        case "scissors":
            if comp == "paper" :
                print("One point for you ")
                user_score += 1
            if comp == "rock" :
                print("One point for me ")
                comp_score += 1
            if comp == "scissors":
                print("Tie")
        case "paper":
            if comp == "rock" :
                print("One point for you ")
                user_score += 1
            if comp == "scissors" :
                print("One point for me ")
                comp_score += 1
            if comp == "paper":
                print("Tie")
        case _:
            print("Maybe you should enter the correct the spelling :)")
            i -= 1
if user_score > comp_score:
    print("You won")
elif user_score < comp_score:
    print("You lost")

        


    
#importing random
import random
#asking user for number of rounds
rounds = int(input("How many rounds do you want "))
for i in range(0,rounds):
    #Asks for users input
    user = input("Choose rock, paper or scissors ").strip()#Removes whitespaces
    # The computer chooses rock,paper,scissors randomly
    comp  = random.choice(["rock","paper","scissors"])
    #Prints users input and the computers random choice
    print(f"You choose {user} and I choose {comp}")

    def play(player1,player2):
        if player1 == "rock" and player2 == "paper":
            print("One point for me")
        elif player1 == "paper" and player2 == "rock":
            print("One point for you")
        elif player1 == "rock" and player2 == "scissors":
            print("One point for you")
        elif player1 == "scissors" and player2 == "rock":
            print("One point for me")
        elif player1 == "scissors" and player2 == "paper":
            print("One point for you")
        elif player1 == "paper" and player2 == "scissors":
            print("One point for me")
        else:
            print("Tie")
    play(user,comp)
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
    def play():
        match user:
            case "rock":
                if comp == "paper" :
                    print("One point for me ")
                if comp == "scissors" :
                    print("One point for you")
                if comp == "rock":
                    print("Tie")   
            case "scissor":
                if comp == "paper" :
                    print("One point for you ")
                if comp == "rock" :
                    print("One point for me ")
                if comp == "scissor":
                    print("Tie")
            case "paper":
                if comp == "rock" :
                    print("One point for you ")
                if comp == "scissors" :
                    print("One point for me ")
                if comp == "paper":
                    print("Tie")
            case _:
                print("Maybe you should enter the correct the spelling :)")
    play()


    # correct the spelling if the word is similar - (rck - rock)
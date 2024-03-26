import random

user_input = input("Choose rock, paper or scissors ").strip()
print(user_input)
comp_input  = random.choice(["rock","paper","scissors"])
print(comp_input)
if user_input == comp_input:
    print("It's a tie then")
elif user_input == "rock" and comp_input == "paper":
    print("One point for me")
elif user_input == "paper" and comp_input == "rock":
    print("One point for you")
elif user_input == "rock" and comp_input == "scissors":
    print("One point for you")
elif user_input == "scissors" and comp_input == "rock":
    print("One point for me")
elif user_input == "scissors" and comp_input == "paper":
    print("One point for me")
else:
    print("One point for me")
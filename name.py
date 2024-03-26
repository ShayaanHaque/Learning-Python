"""
Suppose we are writing a code to take a user's input on a website or web application.
"""
# Takes name from user
name = input("What is your name? ").strip().title()#Removes whitespaces and capitalizis the first character of every word
# splits first and last name of the user's
first,last = name.split()

# Prints user's name
print(f"Hello, {first}")



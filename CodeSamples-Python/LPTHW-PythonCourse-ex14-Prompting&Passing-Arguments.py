# import argv Module from sys
from sys import argv

# parse argv into 2 variables
script, user_name = argv
# declare variable prompt
# prompt = '> '
userInput = ">> "

# print to screen questions to the user and save the input from the 1st response
print(f"Hi, {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes = input(userInput)

#print(f">>>> {userInput}")

# save the user's 2nd response
print(f"Where do you live {user_name}?")
lives = input(userInput)

# print(f">>>> {userInput}")

# save the user's 3rd response
print(f"What kind of computer do you have?")
computer = input(userInput)

# print(f">>>> {userInput}")

# print to screen a confirmation using the inputs from the user
print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer}. Nice.
""")
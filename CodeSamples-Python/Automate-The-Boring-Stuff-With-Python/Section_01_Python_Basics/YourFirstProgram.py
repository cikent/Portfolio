"""This program says hello and asks for the users name and age"""

# Display initial greeting
print('Hello World!')

# Ask the user for their Name and save it as a userName variable
print('What is your name?')
userName = input()

# Greet user by their name and print the length of their name
print('It is good to meet you, ' + userName)
print('Your name is ' + str(len(userName)) + ' characters long!')

# Ask the user for their Age and save it as a userAge variable
print('What is your age?')
userAge = input()

# Print the user's Age 1 year from now
print('You will be ' + str(int(userAge) + 1) + ' on your next Birthday!')

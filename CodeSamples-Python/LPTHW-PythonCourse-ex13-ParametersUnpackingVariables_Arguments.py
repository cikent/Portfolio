# modify script to require arguments when used
from sys import argv

# parse the arguments provided into distinct variables
script, first, second, third = argv

print(">>>> argv=", repr(argv))

# print the 1st argument associated with when the script is run
print("The script is called:", script)
# print the 2nd argument associated with when the script is run
print("Your first variable is:", first)
# print the 3rd argument associated with when the script is run
print("Your second variable is:", second)
# print the 4th argument associated with when the script is run
print("Your third variable is:", third)

# ask the user what they want to do now
userInput = input("\nWhat do you want to do now? ")

# print to screen the value the user provided
print(f"\nSo, you're interested in {userInput} next?! Cool!")

# ask the user their Age
userAge = int(input("\nHow old are you? "))

# print to screen the value the user provided
print(f"\nand you're {userAge} years old?")
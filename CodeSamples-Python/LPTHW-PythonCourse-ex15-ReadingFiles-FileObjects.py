#importing argv module into the script
from sys import argv

# assigning the variables for argv
script, filename = argv

# creating a variable called Txt and assigning it to the contents of filename
txt = open(filename)

# print to screen the file name followed by the contents of the file
print(f"Your file [{filename}] is here:")
print(txt.read())

# print to screen further instructions
print("Type the filename again:")
# save the users input as a variable
fileAgain = input("> ")

# store the contents of the user specified file into a variable
txtAgain = open(fileAgain)

# print to screen the 2nd variable storing content
print(txtAgain.read())

# close both files that have been opened
close(txt)
close(txtAgain)
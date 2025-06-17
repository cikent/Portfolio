# import argv from the sys module
from sys import argv

# parse argv into 2 seperate variables
script, filename = argv

# open filename and save its contents to a string
fileContent = open(filename)

# print to screen a notification to the user
print(f"Here is the Contents of the file: {filename}")

# print to screen the value saved to the variable
print(fileContent.read())

# close the fileObject
fileContent.close()
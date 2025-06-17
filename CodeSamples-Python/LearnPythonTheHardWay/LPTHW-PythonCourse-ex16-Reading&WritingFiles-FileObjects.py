# import the sys module/library
from sys import argv

# delcare the variables argv comprises
script, filename = argv

# notify the user we're going to delete the filename inputted as an argument
print(f"We're going to erase {filename}.")
# print to screen the Hotkey to cancel the script
print("If you don't want that, hit CTRL-C (^C).")
# print to screen the Hotkey to proceed as the script is designed
print("If you do want that, hit RETURN.")

# wait for User input // input doesn't really matter if I'm understanding the logic correctly (except to cancel)
input("?")

# print to screen notification that the script is opening the file
print("Opening the file...")
# open the argv filename and store it into the target variable
target = open(filename, 'w')

# additional prompt for Debug purposes
# input("?")

# print to screen that the script is deleting the contents fo the file
print("Truncate the file. Goodbye!")
target.truncate()

# additional prompt for Debug purposes
# input("?")

# print to screen a question for the user
print("Now I'm going to ask you for three lines.")

# store the string value of whatever the user inputs as Line 1
line1 = input("line 1: ")
# store the string value of whatever the user inputs as Line 2
line2 = input("line 2: ")
# store the string value of whatever the user inputs as Line 3
line3 = input("line 3: ")

# print to screen that the strings will now be saved to file
print("I'm going to write these to the file.")

# write the value stored in line1 to the fileObject
# target.write(line1)
# write a newline in the file to avoid continuation on the previous line
# target.write("\n")
# write the value stored in line2 to the fileObject
# target.write(line2)
# write a newline in the file to avoid continuation on the previous line
# target.write("\n")
# write the value stored in line3 to the fileObject
# target.write(line3)
# write a newline in the file to avoid continuation on the previous line
# target.write("\n")

# study drill #3 from exercise 16 : 1st attempt
# target.write(line1 + "\n" + line2 + "\n" + line3 + "\n")

# study drill #3 from exercise 16 : 2nd attempt
target.write('%s\n%s\n%s\n' % (line1, line2, line3))

# attempts to read contents of fileObject before closing 
# target.flush()
# target.seek(0)
# print(target.read())

# additional prompt for Debug purposes
# input("?")

# print to screen that the fileObject will be closed
print("And finally, we close it.")
# close the fileObject
target.close()

# additional prompt for Debug purposes
# input("?")

# print to screen the contents of the newly written file then close it again
fileContents = open(filename)
print(f"Here of the Contents of {filename}:\n", fileContents.read(), sep='', end='')
fileContents.close()
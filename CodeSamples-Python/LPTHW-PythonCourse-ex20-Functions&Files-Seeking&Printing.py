# import argv from system module
from sys import argv

# unpack argv into different variables
script, input_file = argv

# declare print_all method, which is designed to read whatever fileObject is specified
def print_all(f):
	print(">>> print_all: f=", f)
	print(f.read())
	print("<<< print_all: f=", f)

# seek to the 1st line of the fileObject
def rewind(f):
	print(">>> rewind: f=", f)
	f.seek(0)
	print("<<< rewind: f=", f)

# declare print_a_line method, pass it the line # to read and the fileObject
def print_a_line(line_count, f):
	print(">>> print_a_line: line_count=", line_count)
	print(line_count, f.readline())
	print("<<< print_a_line: line_count=", line_count)

# declare file variable and generate a fileObject from the inputted file
current_file = open(input_file)

# print to screen notification to user that the fileObject will be printed
print("First let's print the whole file:\n")

# print contents of fileObject to screen
print_all(current_file)

# print to screen notification to user that the fileObject will be reset to the start
print("Now let's rewind, kind of like a tape.")

# reset the fileObject state back to the 1st line
rewind(current_file)

# print to screen notification to user that 3 lines will be printed from the fileObject
print("Let's print three lines:")

# declare variable to represent the current line # that has focus & print that line # from the fileObject
current_line = 1
print_a_line(current_line, current_file) # current line is = 1
current_line += 1

# increment the line # then print the line from the fileObject
print_a_line(current_line, current_file) # current line is = 2
current_line += 1

# increment the line # then print the line from the fileObject
print_a_line(current_line, current_file) # current line is = 3
# define the function add
def add(a, b):
	print(f"ADDING {a} + {b}")
	return a + b

# define the function subtract
def subtract(a, b):
	print(f"SUBTRACTING {a} - {b}")
	return a - b

# define the function multiply
def multiply(a, b):
	print(f"MULTIPLYING {a} * {b}")
	return a * b

# define the function divide
def divide(a, b):
	print(f"DIVIDING {a} / {b}")
	return a / b

# print to screen a prompt about the following methods/functions being called
print("Let's do some math with just functions!")

# execute the functions
age = add(30, 5) # == 35
height = subtract(78, 4) # == 74
weight = multiply(90, 2) # == 180
iq = divide(100, 2) # == 50

# print to screen the values of each of the variables
print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")


# A puzzle for the extra credit, type it in anyway.
# Puzzle #1
print("Here is the puzzle.")

puzzle1 = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print("That becomes: ", puzzle1, "Can you do it by hand?")

# Study Drill 3
print("Here is the puzzle.")

studyDrill3 = multiply(height, divide(weight, add(iq, subtract(age, 10))))
# puzzle2 == 177.6
print("That becomes: ", studyDrill3, "Can you do it by hand?")

# Study Drill 4
print("Here is the puzzle.")

studyDrill4 = divide(height, subtract(age, multiply(iq, add(weight, 10))))

print("That becomes: ", studyDrill4, "Can you do it by hand?")
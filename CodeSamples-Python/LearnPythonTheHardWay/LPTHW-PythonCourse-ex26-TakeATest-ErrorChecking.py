# import Argv module from System's Library
from sys import argv

# unpack Argv into its separate parameters
script, filename = argv

# open the File object and create a instance for manipulation
txt = open(filename)

# Ask the User for their Age and save the input returned
print("How old are you?", end=' ')
age = input()
# Ask the User for their Height and save the input returned
print("How tall are you?", end=' ')
height = input()
# Ask the User for their Weight and save the input returned
print("How much do you weigh?", end=' ')
weight = input()

# print to screen the User's collective input from the 3 previous quetions
print(f"So, you're {age} old, {height} tall and {weight} heavy.")

# print fString to Screen indicating the File's name
print(f"Here's your file {filename}:")
# print to screen the contents of the file object
print(txt.read())

# print to screen a question asking the User to input the name of the file again.
print("Type the filename again:")
file_again = input("> ")

# open the file object and create a instance for manipulation
txt_again = open(file_again)

# print to screen the contents of the file object
print(txt_again.read())

# print to a screen multiple lines with seperate print functions using Escape characters for New Lines and Tabs
print('Let\'s practice everything.')
print('You\'d need to know \'bout escapes.') 
print('with \\ that do \n newlines and \t tabs.')

# Create a multi-line String Variable using New Lines and Tabs
poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\twhere there is none.
"""

# print to screen the String Variable saved from before
print("--------------")
print(poem)
print("--------------")

# Creat an Integer object and assign it the value of 5
five = 10 - 2 + 3 - 6
# Print to screen an F String formatting the Variable created to display its actual value
print(f"This should be five: {five}")

# create the Function secret formula for calculating the # of Jelly Beans that can fit into a Jar or Crate
def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates

# Create the an Integer Variable and assign its value
start_point = 10000
# run the Secret_Formula function to generate the values for Jelly Beans, Jars and Crates
jelly_beans, jars, crates = secret_formula(start_point)

# print to a Format String having formatted the Start Point variable's value
# remember that this is another way to format a string
print("With a starting point of: {}".format(start_point))
# print to a Format String having formatted the Jelly beans, Jars and Crates variable's value
# it's just like with an f"" string
print(f"We'd have {jelly_beans} jelly beans, {jars} jars, and {crates} crates.")

# Execute the same calcutions prior but @ 10% of the prior values
start_point = start_point / 10

print("We can also do that this way:")
formula = secret_formula(start_point)
# this is an easy way to apply a list to a format string
print("We'd have {} beans, {} jars, and {} crates.".format(*formula))


# Define new Integer variables and assign their values
people = 20
cats = 30
dogs = 15

'''
Print to screen the Text if the operator logic evaluates to True & modify
the logic such that it would be accurate respective to what Text indicates
'''
if people < cats:
    print("Too many cats! The world is doomed!")

# Print to screen the Text if the Logic is True
if people > cats:
    print("Not many cats! The world is saved!")

if people < dogs:
    print("The world is drooled on!")

if people > dogs:
    print("The world is dry!")

# modify the existing dogs variable to be 5 greater in value
dogs += 5

if people >= dogs:
    print("People are greater than or equal to dogs.")

if people <= dogs:
    print("People are less than or equal to dogs.")

if people == dogs:
    print("People are dogs.")
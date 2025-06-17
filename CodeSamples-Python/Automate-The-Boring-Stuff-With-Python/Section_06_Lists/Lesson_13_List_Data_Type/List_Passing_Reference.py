# Define a function to append Hello to lists
def eggs(someParameter):
    someParameter.append('Hello')

# Declare a list named spam
spam = [1, 2, 3]

# Run Eggs and pass spam as the argument
eggs(spam)

# Print to screen the value of spam
print(spam)

""" someInt = 13
eggs(someInt)                   # Will throw Error because Integer objects cannot be appended
print(someInt)

someString = 'This is a string'
eggs(someString)                # Will throw Error because String objects cannot be appended
print(someString) """


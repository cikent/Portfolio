# Define a function called spam
def spam():
    # Set eggs to a Local String
    eggs = 'spam local'
    print(eggs)  # prints 'spam local'


# Define a function called bacon
def bacon():
    # Set eggs to a Local String
    eggs = 'bacon local'
    print(eggs)  # prints 'bacon local'
    # call spam
    spam()       # prints 'spam local'
    print(eggs)  # prints 'bacon local'


# Set eggs to a Global String
eggs = 'eggs global'
# Call the function bacon()
bacon()
print(eggs)  # prints 'eggs global'

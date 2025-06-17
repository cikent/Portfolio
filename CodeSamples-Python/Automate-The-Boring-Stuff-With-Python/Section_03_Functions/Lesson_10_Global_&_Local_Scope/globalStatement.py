# Define spam
def spam():
    # Declare the variable eggs Globally
    global eggs
    # Set the Global variable eggs to 'spam'
    eggs = 'spam'

# Define the Global variable eggs
eggs = 'global'

# Call the spam function
spam()

# Print the Global eggs variable value
print(eggs)
# Define spam: Calls a Global Variable and updates the value locally
def spam():
    global eggs
    print(eggs)
    eggs = 'Globally defined variable, updated in Local scope'      # This variable has Global Scope
    print(eggs)

# Define bacon
def bacon():
    eggs = 'Locally defined variable, but never called'             # This variable has Local Scope
    
# Define ham
def ham():
    print(eggs)                                                     # This variable has Global Scope

# Declare the variable eggs Globally
eggs = 42   

# Print value of eggs
print(eggs)                                                        # This variable has Global Scope

# Call spam and update the Global variable value for eggs
spam()

# Print value of eggs
print(eggs)                                                         # This variable has Global Scope

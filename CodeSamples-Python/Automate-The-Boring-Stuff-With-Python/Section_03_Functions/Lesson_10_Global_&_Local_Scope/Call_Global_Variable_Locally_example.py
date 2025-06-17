# Define spam
def spam():
    # Call the print function and pass in the Global variable
    print(eggs)


# Define eggs at the Global scope
eggs = 'global variable, defined in Global scope'
spam()

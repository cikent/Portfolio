# Declare an empty List called catNames
catNames = []

while True:
    # Ask the User for the Catz name?
    print("Enter the name of cat " + str(len(catNames) + 1)
        + " (Or enter nothing to stop.):")
    # Store the User's response 
    name = input()
    # Evaluate User's response; If blank, break and exit the While loop
    if name == "":
        break
    # Update catNames by appending the new name to the end of the list
    catNames = catNames + [name]  

# Print the Cat names after the break in the While loop 
print("The cat names are:")
for name in catNames:
    print("    " + name)


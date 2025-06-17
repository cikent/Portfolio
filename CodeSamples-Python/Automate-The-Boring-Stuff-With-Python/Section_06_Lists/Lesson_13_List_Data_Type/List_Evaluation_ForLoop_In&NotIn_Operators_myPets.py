# Create a list of Pets
myPets = ["Bones", "Gunner", "Nymeria", "Dina"]

# Ask the User to provide a Pet name
print("Please enter a pet name: ")
# Store the input inside a String variable
name = str(input())
# Detemine if the name matches one already in the list
if name not in myPets:                      # The 'in' or 'not in' operator returns a True or False result 
    print("I do not have a pet named " + name)
else:
    print("Great guess, " + name + " is one of my pets!")

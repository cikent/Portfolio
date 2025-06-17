# import module
import random

# Define a List variable
myPets = ['Bones', 'Dina', 'Fish', 'Gunner', 'Nymeria']

# Print to console, myPets
print('\nDebug: Print the List "myPets"')
print(myPets)

# Example 1: Randomly select an item from the List
print('\nDebug: Print a random item from "myPets" using random.choice')
print(random.choice(myPets))

# Example 2: Randomly select an item from the List (this version is a longer version of Example 1)
print('\nDebug: Print a random item from "myPets" using random.randint()')
print(myPets[random.randint(0, len(myPets))-1])

# Example 3: Randomly shuffle the items in the List
print('\nDebug: Print the List "myPets", then print again after it has been shuffled using random.shuffle()')
random.shuffle(myPets)
print(myPets)

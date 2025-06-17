"""
Description: List values have an index() method that can be passed a value, 
and if that value exists in the list, the index of the value is returned. 
If the value isn’t in the list, then Python produces a ValueError error.
Source: https://automatetheboringstuff.com/2e/chapter4/#calibre_link-169
"""
# Create a List for my pets
myPets = ['Bones', 'Gunner', 'Nymeria', 'Dina']
# Print the List and the Index value for an Item in the list 
print('Debug: Print to console, the Index value for Gunner: ' + str(myPets.index('Gunner')))

"""
When there are duplicates of the value in the list, the index of its first appearance is returned. 
Enter the following into the interactive shell, and notice that index() returns 2, not 4:
"""
# Create a 2nd List for my pets
myPets2 = ['Bones', 'Gunner', 'Nymeria', 'Dina', 'Nymeria']
# Print the List and the Index value for an Item in the list, only the 1st instance in the List is returned
print('Debug: Print to console, the Index value for Nymeria: ' + str(myPets.index('Nymeria')))
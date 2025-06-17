"""
Description: The del statement is good to use when you know the index of the value you want to remove
from the list. The remove() method is useful when you know the value you want to remove from the list.
Source: https://automatetheboringstuff.com/2e/chapter4/#calibre_link-172
"""

# Declare a List value
diablo3Classes = ['Barbarian', 'Crusader', 'Demon Hunter', 'Monk', 'Necromancer', 'Witch Doctor', 'Wizard']
print('Print the initial list: \n' + str(diablo3Classes))

# Remove an item from the List
diablo3Classes.remove('Barbarian')
print('\nThe remove() method deletes an item from the list based upon the value specified, Barbarian in this case: \n' + str(diablo3Classes))

# Delete an item from the List
del diablo3Classes[0]
print('\nThe del statement deletes an item from the list based upon the Index specified, 0 in this case: \n' + str(diablo3Classes))

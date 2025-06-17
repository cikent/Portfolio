"""
Description: sort() uses “ASCIIbetical order” rather than actual alphabetical order for sorting strings. This means uppercase letters come before lowercase letters. Therefore, the lowercase a is sorted so that it comes after the
uppercase Z.

If you need to sort the values in regular alphabetical order, pass str.lower for the key keyword argument in the sort() method call.

You can also pass True for the reverse keyword argument to have sort() sort the values in reverse order. 
Source: https://automatetheboringstuff.com/2e/chapter4/#calibre_link-172
"""

# Declare a List value
diablo3Classes = ['Witch Doctor', 'Demon Hunter', 'Monk', 'Wizard', 'Necromancer', 'Crusader', 'Barbarian']
print('Print the initial list: \n' + str(diablo3Classes))

# Sort the List
diablo3Classes.sort()
print('\nThe sort() method returns the list in ascending order: \n' + str(diablo3Classes))

# Reverse Sort the List
diablo3Classes.sort(reverse=True)
print('\nThe sort(reverse=True) method returns the list in descending order: \n' + str(diablo3Classes))

# Declare a new List value
diablo3_diablo2Classes = ['paladin', 'sorceress', 'amazon', 'necromancer', 'assassin', 'barbarian', 'druid', 'Witch Doctor', 'Demon Hunter', 'Monk', 'Wizard', 'Necromancer', 'Crusader', 'Barbarian']
print('\nPrint the new list: \n' + str(diablo3_diablo2Classes))

# Sort the List in actual alphabetical order
diablo3_diablo2Classes.sort(key=str.lower)
print('\nThe sort(key=str.lower) method returns the list in alphabetical order: \n' + str(diablo3_diablo2Classes))
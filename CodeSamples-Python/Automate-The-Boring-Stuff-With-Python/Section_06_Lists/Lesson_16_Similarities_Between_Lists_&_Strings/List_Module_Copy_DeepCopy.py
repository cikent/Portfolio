"""
The copy Module’s copy() and deepcopy() Functions
-------------------------
Description: Although passing around references is often the handiest way to deal with lists and dictionaries, if the function modifies the list or dictionary that is passed, you may not want these changes in the original list or dictionary value. For this, Python provides a module named copy that provides both the copy() and deepcopy() functions. The first of these, copy.copy(), can be used to make a duplicate copy of a mutable value like a list or dictionary, not just a copy of a reference.

Source: https://automatetheboringstuff.com/2e/chapter4/#calibre_link-182
"""
import copy

#Declare a List
spam = ['A', 'B', 'C', 'D']

#Print the new List Id value to the screen
print(f'Declare the 1st List: {spam}\nThen print the Id value of the 1st variable to the screen:')
print(id(spam))

#Declare a 2nd List that is a copy of the 1st List
cheese = copy.copy(spam)

#Print the new List Id value to the screen
print(f'\nDeclare a 2nd List: {cheese} that is a copy of the 1st List\nThen print the Id value of the 2nd variable to the screen:')
print(id(cheese))

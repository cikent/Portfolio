"""
Description: Methods belong to a single data type. The append() and insert() methods are list methods
 and can be called only on list values, not on other values such as strings or integers.
Source: https://automatetheboringstuff.com/2e/chapter4/#calibre_link-172
"""

# Declare a List variable
d2TPActiveUser = ['Athar', 'Drahgo', 'Xena']
print('Print the initial list: \n' + str(d2TPActiveUser))

# Append a value to the end the List
d2TPActiveUser.append('Vladimir')
print('The append() method add\'s a new value to the end of the list: \n' + str(d2TPActiveUser))

# Insert a value into List
d2TPActiveUser.insert(1, 'Krador')
print('The insert() method add\'s a new value at any Index specified, 1 in this case: \n' + str(d2TPActiveUser))

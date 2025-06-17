"""
Sequence Data Types
-------------------------
Description: Lists aren’t the only data types that represent ordered sequences of values. For example, strings and lists are actually similar if you consider a string to be a “list” of single text characters. The Python sequence data types include lists, strings, range objects returned by range(), and tuples (explained in the “The Tuple Data Type” on page 96). Many of the things you can do with lists can also be done with strings and other values of sequence types: indexing; slicing; and using them with for loops, with len(), and with the in and not in operators.

Source: https://automatetheboringstuff.com/2e/chapter4/#calibre_link-175
"""

# Declare a String variable
name = 'Inciter'

# Print to Console: Each index within the List passed 
for i in name:
    print('* * * ' + i + ' * * *')

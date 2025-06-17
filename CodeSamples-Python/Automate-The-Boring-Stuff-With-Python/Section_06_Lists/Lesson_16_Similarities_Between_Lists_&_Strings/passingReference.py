"""
Passing References
-------------------------
Description: References are particularly important for understanding how arguments get passed to functions. When a function is called, the values of the arguments are copied to the parameter variables. For lists (and dictionaries, which I’ll describe in the next chapter), this means a copy of the reference is used for the parameter.

Source: https://automatetheboringstuff.com/2e/chapter4/#calibre_link-181
"""

# Define the function eggs
def eggs(someParameter):
    someParameter.append('Hello')

spam = [1, 2, 3]
eggs(spam)
print(spam)

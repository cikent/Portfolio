"""
Requirements: 
1. Creat a function that takes a List as an Argument
2. Return a String with all the Items in the List concatenated by: ', ' (Comma & a Space)
3. Insert 'and' before the last Item is concatenated with the String
4. Function should be able to work with any List value pass to it

Source: https://automatetheboringstuff.com/chapter4/ -> search for Comma Code
"""

# Sample test lists
spamText = ['apples', 'bananas', 'tofu', 'cats']
baconNumber = [1, 2, 3, 4, 5]


# Define a function to take a List as a Parameter and concatenate the values of the List Reference together
def mergeList(anyList):
    # Declare an empty String    
    mergeWords = str('')
    # For each word in the List, add it to mergeWords unless its the last index
    for item in anyList:
        # If the item is not the last Index, then add the item followed by a Comma and a space 
        if item != anyList[-1]:
            mergeWords += str(item) + ', '
        # If the item is the last Index, then add 'and' followed by the last item in the list
        else: 
            mergeWords += 'and ' + str(item)
    # Return the new value of mergeWords
    return mergeWords

# Debug print statement to verify contents of variables are stored correctly
print(spamText)
print(baconNumber)

# Create new variables to hold the String value that mergeList will output
newMessage = mergeList(spamText)
newMessage2 = mergeList(baconNumber)


# Print the value stored in the String variables
print(newMessage)
print(newMessage2)

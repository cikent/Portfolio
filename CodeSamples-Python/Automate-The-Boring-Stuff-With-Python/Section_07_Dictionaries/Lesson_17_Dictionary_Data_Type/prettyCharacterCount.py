# Import Pprint and Pformat modules
import pprint

# Define a String
message = 'It was a bright cold day in April, and the clocks were stricking thirteen.'

# Define a empty Dictionary
count = {}

# Iterate through each character within the String 
for character in message:
    # Create a Key/value pair in the Count Dict for each unique Character value in message
    count.setdefault(character, 0)
    # Set the value of each Unique Key equal to the # of times that character is utilized within message
    count[character] = count[character] + 1

# Using the module Pprint's Pprint function, print to screen the value of Count in a nicely formatted style 
pprint.pprint(count)

# Using the module Pprint's pformat function, replicate the previous Pprint output using Pformat instead
print(pprint.pformat(count))

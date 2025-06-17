# Declare a variable and set it value to an empty string
name = ''

# Execute block when the name variable doesn't equal 'your name'
while name != 'your name':
    # Ask the user to input 'your name'
    print('Please type: your name.')
    # Update name variable based upon user's input
    name = input()          # Input functions default output is as a String DataType

# Exit While loop and print if user updated name's value correctly
print('Thank you!')

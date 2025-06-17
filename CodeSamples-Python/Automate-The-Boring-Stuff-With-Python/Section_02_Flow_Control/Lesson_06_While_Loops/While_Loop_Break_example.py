# Declare a variable and set it value to an empty string
name = ''

# Execute block when the name variable doesn't equal 'your name'
while True:
    # Ask the user to input 'your name'
    print('Please type: your name.')
    # Update name variable based upon user's input
    name = input()          # Input functions default output is as a String DataType
    if name == 'your name':
        break

# Print once the user has updated the name value correctly
print('Thank you!')

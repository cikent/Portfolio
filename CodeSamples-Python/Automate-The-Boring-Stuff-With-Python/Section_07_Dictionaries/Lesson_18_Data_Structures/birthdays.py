# Define a Dictionary to save the Birthday's of family
birthdays = {'Kaleb': 'Jan 10th', 'Nicole': 'May 20th', 'Ivy': 'May 27th', 'Chris': 'Jul 15th'}

# Execute continuously until User enters nothing and the script exits
while True:
    
    # Ask the User to input a Name
    print('Enter a name: (blank to quit)')
    
    # Try clause to ensure the User inputs a valid entry
    try:
        # Save the User's input
        name = str(input())
    except:
        # Prompt the User to retry if they input an invalid value
        print('You didn\'t input a person\'s name, please try again.')
    # Evaluate if the User entered anything
    if name == '':
        # If User entered nothing, exit script entirely
        break
    # Determine if the User's input matches a name preexisting within the Dictionary
    if name in birthdays:
        # If the name exists, print the Birthday(value) paired with the name(Key)
        print(birthdays[name] + ' is the birthday of ' + name)
    else:
        # Otherwise, inform the User that name is not Stored
        print('I do not have birthday information for ' + name)
        print('What is their birthday?')
        # Verify the User's input for the Birthday value is a String
        try:
            bday = str(input())
        except:
            print('That is not a valid Birthday. Please input their Birthday in the following format: 3 Letter Month & Day. Example: Jul 15')
        # If User's input is a valid String, save it to the Birthday's Dictionary
        birthdays[name] = bday
        # Notify the User the Dictionary has been updated
        print('Birthday database updated.')
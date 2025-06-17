# Import the Library: random
import random

# Declare a list of messages
messages = ['It is certain',
    'It is decidedly so',
    'Yes definitely',
    'Reply hazy try again',
    'Ask again later',
    'Concentrate and ask again',
    'My reply is no',
    'Outlook not so good',
    'Very doubtful']

# Print a random value from the list ranging between 0 and 8 (9 Total)
print(messages[random.randint(0, len(messages) - 1)])

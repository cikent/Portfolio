# Import the random module/library
import random

# define a Magic 8 Ball function
def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'It is certain'
    elif answerNumber == 2:
        return 'It is decidedly so'
    elif answerNumber == 3:
        return 'Yes'
    elif answerNumber == 4:
        return 'Reply hazy try again'
    elif answerNumber == 5:
        return 'Ask again later'
    elif answerNumber == 6:
        return 'Concentrate and ask again'
    elif answerNumber == 7:
        return 'My reply is no'
    elif answerNumber == 8:
        return 'Outlook not so good'
    elif answerNumber == 9:
        return 'Very doubtful'

# declare a integer variable randomly between 1 to 9 each time the program is called
# r = random.randint(1, 9)

# create a new String variable based upon the Random # and the getAnswer function
# fortune = getAnswer(r)

# print the fortune variable
# print(fortune)

# combining the 3 expressions from line 28 to 35 into a single expression
print(getAnswer(random.randint(1, 9)))

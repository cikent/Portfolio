# Extra Credit: Create another Error to indicate when the User has inputted a negative number
print('How many cats do you have?')
numCats = input()

try:
    if int(numCats) > 0:
        try:
            if int(numCats) >= 4:
                print('That is a lot of cats.')
            else:
                print('That is not that many cats.')
        except ValueError:
            print('You did not enter a positive number.')           # Not executing... need to find out why
except ValueError:
    print('You did not enter a number.')
    
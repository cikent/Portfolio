# Define the Collatz Sequence
def collatz(number):
    # Determine if the number passed is even
    if number % 2 == 0:            
        print(number // 2)          
        return number // 2
    # If not even, it must be odd
    else:
        print((3 * number) + 1)
        return (3 * number) + 1


# Ask user to choose a #
def askUserForNumber():
    while True:
        try:
            # Continually ask the User to provide a whole number and save the value as a variable
            userNumber = int(input("Please input any whole number: "))
            # Return userNumber
            return userNumber
        except ValueError:
            # Inform the User that they inputted a non-valid value. Then ask them to try again.
            print("That was not a whole number (Integer), please try again: ")


# Save the User's chosen number as the Collatz value
collatzNumber = askUserForNumber()

# Execute while Collatz Number != 1
while collatzNumber != 1:
    # Update collatzNumber with the collatz() Function/Method's return value
    collatzNumber = collatz(collatzNumber)

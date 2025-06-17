# Declare the variable spam and set it to the Integer value of 0
spam = 0
# Execute While Loop while spam is less than 5
while spam < 5:
    # Increment the spam value by 1
    spam = spam + 1
    # Evaluate if the spam value equals 3
    if spam == 3:
        # Re-evaluate the while loop condition with continue 
        continue
    # Print spam's present value to the console
    print('spam is ' + str(spam))

# Define div42by
def div42by(divideBy):
    while True:
        try:
            return 42 / divideBy
        except ZeroDivisionError:
            # Updated the Exception to be in scope of a 'while clause' and ask user to provide new value before trying again
            divideBy = int(input('Error: Invalid argument. Please input another # that is not zero: '))
            continue
        except:
            print('There was an unknown error, please try again.')


print(div42by(2))
print(div42by(12))
print(div42by(0))                      # ERROR! --This will cause the exception
print(div42by(1))
print(div42by(7))

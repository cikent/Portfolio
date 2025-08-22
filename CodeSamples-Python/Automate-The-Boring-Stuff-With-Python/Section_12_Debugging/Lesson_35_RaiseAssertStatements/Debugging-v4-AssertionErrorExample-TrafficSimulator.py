# You can raise your own exceptions: raise Exception(‘This is the error message.')
# You can also use assertions: assert condition, ‘Error message'
# Assertions are for detecting programmer errors that are not meant to be recovered from. User errors should raise exceptions.

# Create a Dictionary to represent a Stoplight @ Market 2nd Stree, North / South is Green, East / West is Red
market_2nd = {'ns': 'green', 'ew': 'red'}

def switchLights(intersection):
    for key in intersection.keys():
        if intersection[key] == 'green':
            intersection[key] = 'yellow'
        elif intersection[key] == 'yellow':
            intersection[key] = 'red'
        elif intersection[key] == 'red':
            intersection[key] = 'green'
    # Create an Assertion Error to ensure a Light doesn't turn Green until the other Light is Red
    assert 'red' in intersection.values(), 'Neither light is red!' + str(intersection)

# Print value to screen
print(market_2nd)

# Call the switchLights() function to Change the Stop Lights
switchLights(market_2nd)

# Print value to screen
print(market_2nd)
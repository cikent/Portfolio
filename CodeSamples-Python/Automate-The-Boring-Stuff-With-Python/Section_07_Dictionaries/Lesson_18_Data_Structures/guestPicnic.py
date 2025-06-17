# Define a Dictionary of Guests and Items they're bringing
allGuests = {'Alice': {'apples': 5, 'pretzels': 12},
'Bob': {'ham sandwiches': 3, 'apples': 2},
'Carol': {'cups': 3, 'apple pie': 1}}

# Define a Function to Count the # of Items someone brought
def totalBrought(guests, item):
    numBrought = 0
    for k, v in  guests.items():
        numBrought = numBrought + v.get(item, 0)
    return numBrought

# Print to screen the items brought by everyone
print('Number of things being brought:')
print(' - Apples ' + str(totalBrought(allGuests, 'apples')))
print(' - Cups ' + str(totalBrought(allGuests, 'cups')))
print(' - Cakes ' + str(totalBrought(allGuests, 'cakes')))
print(' - Ham Sandwiches ' + str(totalBrought(allGuests, 'ham sandwiches')))
print(' - Apple Pies ' + str(totalBrought(allGuests, 'apple pies')))
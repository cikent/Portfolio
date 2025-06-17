# Declare spam as a List
spam = [0, 1, 2, 3, 4, 5]
# Declare cheese and assign it to spam's List Reference
cheese = spam

# Update the List Reference value using cheese
cheese[1] = 'Hello!'

# Both spam && cheese have the same List Reference value
print(spam)
print(cheese)

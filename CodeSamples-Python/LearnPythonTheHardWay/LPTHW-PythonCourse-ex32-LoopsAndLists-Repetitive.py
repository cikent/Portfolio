# declare 3 lists and assign values to the entities
the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# Study Drill #3 example
fruits_length = len(fruits)
copy_fruits = fruits.copy()

# Study Drill #3 example
print(f"This is the # of entities in 'copy_fruits': {copy_fruits}")

# Study Drill #3 example
copy_fruits.clear()

# Study Drill #3 example
print(f"This is the # of entities in 'copy_fruits': {copy_fruits}")

# this first kind of for-loop goes through a list
for number in the_count:
	print(f"This is count {number}")

# same as above
for fruit in fruits:
	print(f"A fruit of type: {fruit}")

# also we can go through mixed lists too
for i in change:
	print(f"I got {i}")

# we can also build lists, first start with an empty one
elements = []

# then use the range function to do 0 to 5 counts
for i in range(0, 6):
	print(f"Adding {i} to the list.")
	# append is a function that lists understand
	elements.append(i)

# now we can print them out too
for i in elements:
	print(f"Elements was: {i}")
# declare an increment variable
i = 0
# declare the empty list called numbers
numbers = []

# create a While Loop that will execute forever while i is less than 6
while i < 6:
	# print to screen a format string for the element in the list with Focus
	print(f"At the top i is {i}")
	# add the value of i to the end of the numbers list
	numbers.append(i)

	# increment i by 1
	i += 1
	# print to screen the contents of the List numbers
	print("Numbers now: ", numbers)
	# print to screen a format string for the element in the list with Focus
	print(f"At the bottom i is {i}")

# print to screen a String
print("The numbers: ")

# create a For Loop for each of the elements in numbers
for num in numbers:
	# print to screen each element within the list numbers
	print(num)
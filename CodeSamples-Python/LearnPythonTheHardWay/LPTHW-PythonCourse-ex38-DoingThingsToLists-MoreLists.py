# create a string variable and assign it a value
ten_things = "Apples Oranges Crows Telephone Light Sugar"

# print to screen a prompt
print("Wait there are not 10 things in that list. Let's fix that.")

# create the List variable 'stuff' by parsing the string variable ten_things
stuff = ten_things.split(' ')
# create another list and fill it with string object variables
more_stuff = ["Day", "Night", "Song", "Frisbee",
			  "Corn", "Banana", "Girl", "Boy"]

# execute while stuff does not equal 10 entities
while len(stuff) != 10:
	next_one = more_stuff.pop() # 
	print("Adding: ", next_one)
	stuff.append(next_one)
	print(f"There are {len(stuff)} items now.")

print("There we go: ", stuff)

print("Let's do some things with stuff.")

print(stuff[1])
print(stuff[-1]) # whoa! fancy
print(stuff.pop())
print(' '.join(stuff)) # what? cool!
print('#'.join(stuff[3:5])) # super stellar!
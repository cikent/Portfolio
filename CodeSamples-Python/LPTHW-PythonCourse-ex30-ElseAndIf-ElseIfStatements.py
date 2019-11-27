# declare Integer Variables to hold values
people = 30
cars = 40
trucks = 15

# Logic Gate: is Car's more than People, if True, execute underlying block of code
if cars > people:
	print(f">>>>: cars = {cars}")
	print(f">>>>: people = {people}")
	print("We should take the cars.")

# Logic Gate: is People more than Cars, if True, execute underlying block of code
elif cars < people:
	print(f">>>>: cars = {cars}")
	print(f">>>>: people = {people}")
	print("We should not take the cars.")

# Logic Gate: If proceeding If's fail, execute underlying block of code
else:
	print("We can't decide.")

# Logic Gate: is Trucks's more than Cars, if True, execute underlying block of code
if trucks > cars:
	print("That's too many trucks.")

# Logic Gate: is Cars's more than Trucks, if True, execute underlying block of code
elif trucks < cars:
	print("Maybe we could take the trucks.")

# Logic Gate: If proceeding If's fail, execute underlying block of code
else:
	print("We still can't decide.")

# Logic Gate: is People more trhan Trucks, if True, execute underlying block of code
if people > trucks:
	print("Alright, let's just take the trucks.")

# Logic Gate: If proceeding If's fail, execute underlying block of code
else:
	print("Fine, let's stay home then.")


# increment the values of the variables
people += 5
cars -= 10
trucks *= 2

# Logic Gate: If, elif, else statement to determine whether or not all the vehicles have a driver
if people > cars + trucks:
	print("There are enough people for each vehicle to be driven!")

elif people < cars + trucks:
	print("There isn't enough people to drive all the vehicles.")

else:
	print("There is exactly one driver for each vehicle.")
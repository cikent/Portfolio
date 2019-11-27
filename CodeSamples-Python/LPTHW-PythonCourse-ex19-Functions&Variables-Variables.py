# define the function cheese_and_crackers, it requires 2 arguments when run/use/called
# def cheese_and_crackers(cheese_count, boxes_of_crackers):
# 	print(f"You have {cheese_count} cheeses!")
# 	print(f"You have {boxes_of_crackers} boxes of crackers!")
# 	print("Man that's enough for a party!")
# 	print("Get a blanket. \n")

# run cheese_and_crackers using integers as arguments
# print("We can just give the function numbers directly:")
# cheese_and_crackers(20, 30)

# run cheese_and_crackers using variables as agruments
# print("OR, we can use variables from our scripts:")
# amount_of_cheese = 10
# amount_of_crackers = 50

# cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# run cheese_and_crackers using integers + math as arguments
# print("We can even do math inside too:")
# cheese_and_crackers(10 + 20, 5 + 6)

# run cheese_and_crackers using variables + integers + math as arguments
# print("And we can combine that two, variables and math:")
# cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

# =======================================================================================
# Exercise 19 Study Drill # 3
# =======================================================================================
from datetime import date

currentDate = str(date.today())
currentYear = int(currentDate[:4])
currentMonth = int(currentDate[5:7])
currentDay = int(currentDate[-2:])

print(">>>> currentDate: ", repr(currentDate))
print(">>>> currentYear: ", repr(currentYear))
print(">>>> currentMonth: ", repr(currentMonth))
print(">>>> currentDay: ", repr(currentDay))

def name_and_age(userName, userBirthday):
	# parse the User's age
	userBirthYear = int(userBirthday[-4:])
	userBirthMonth = int(userBirthday[:2])
	userBirthDay = int(userBirthday[2:4])

	print(">>>> userBirthYear: ", repr(userBirthYear))
	print(">>>> userBirthMonth: ", repr(userBirthMonth))
	print(">>>> userBirthDay: ", repr(userBirthDay))

	# calculate the # of years since birth
	if (currentMonth >= userBirthMonth) & (currentDay >= userBirthDay):
		userYearAge = abs(currentYear-userBirthYear)
	else:
		userYearAge = abs((currentYear-userBirthYear)-1)
	
	# calculate the # of months since birth
	if (currentMonth >= userBirthMonth) & (currentDay >= userBirthDay):
		userMonthAge = abs(currentMonth-userBirthMonth)
	else:
		userMonthAge = abs(abs(currentMonth-userBirthMonth)-12)
	
	# calculate the # of days since birth
	if currentDay >= userBirthDay:
			userDayAge = abs(currentDay-userBirthDay)
	else:
		if currentMonth == (1 or 3 or 5 or 7 or 8 or 10 or 12):
			userDayAge = abs(abs(currentDay-userBirthDay)-31)
		elif currentMonth == (4 or 6 or 9 or 1):
			userDayAge = abs(abs(currentDay-userBirthDay)-30)
		else:
			userDayAge = abs(abs(currentDay-userBirthday)-28)

	# print to screen the user's name and age
	print(f"So your name is {userName} and you are currently {userYearAge} years, {userMonthAge} months and {userDayAge} days old!?")


userName = str(input("What is your name?: "))
userBirthday = str(input("What year were you born?\nPlease enter it in the following format \"MMDDYYYY\": "))


# name_and_birthday(userName, userBirthyear)
name_and_age(userName, userBirthday)


'''
Known Defects:
1) If User B-day is greater than present day but in the same Month; month is calculated wrong
2) 

'''
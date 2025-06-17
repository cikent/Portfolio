# declare and set the # of Cars available for the trip
cars = 100
# declare and set the Space available in each car
space_in_cars = 4.0
# declare and set the # of Drivers available for commuting
drivers = 30
# declare and set the # of passengers that need transportation
passengers = 90
# declare and set the # of cars that won't be driven due to missing Drivers
cars_not_driven = cars - drivers
# declare and set the # of Cars that will have Drivers available
cars_driven = drivers
# declare and set the capacity in each vehicle for carpooling
carpool_capacity = cars_driven * space_in_cars
# declare and set the Average # of passengers per car
average_passengers_per_car = passengers / cars_driven

# print information to screen
print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")
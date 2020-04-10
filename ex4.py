# Define numbers of cars
cars = 100
# Define car capacity
space_in_a_car = 4  # corrected after Study Drill 2
# Define Drivers
drivers = 30
# Define number of passangers
passengers = 90
# Calculate available cars
cars_not_driven = cars - drivers
# I don't know what is it for. Just a variable assign
cars_driven = drivers
# Calculate carpool capacity
carpool_capacity = cars_driven * space_in_a_car
# Calculate average
average_passangers_per_car = passengers / cars_driven


print("There are ", cars, "cars available.")
print("There are only ", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passangers_per_car, "in each car.")
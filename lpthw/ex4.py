# Exercise 4: Variables and Names

cars = 100
space_in_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_car
average_passengers_per_car = passengers / cars_driven

print('There are', cars, 'cars available.')
print('There are only', drivers, 'drivers available.')
print('There will be', cars_not_driven, 'empty cars today.')
print('We can transport', carpool_capacity, 'people today.')
print('We have', passengers, 'to carpool today.')
print('We need to put about', average_passengers_per_car, 'in each car.')


# Study Drills
# 1. I used 4.0 for space_in_car, but is that necessary? What happens if it's 
#    just 4?
# 2. Remember that 4.0 is a "floating point" number. Find out what that means.
# 3. Write comments above each of the variable assignments.
# 4. Make sure you know what "=" is called (equals) and that it's making names 
#    for things.
# 5. Remember "_" is an underscore character.
# 6. Try running python as a calculator like you did before and use variable 
#    names to do your calculations.

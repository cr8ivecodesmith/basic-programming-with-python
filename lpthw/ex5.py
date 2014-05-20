# Exercise 5: More variables and printing

my_name = 'Matt Lebrun'
my_age = 27  # Not a lie
my_height = 165.1  # cm
my_weight = 63.5  # kg
my_eyes = 'Dark Brown'
my_teeth = 'White'
my_hair = 'Shaved'

print("Let's talk about %s" % my_name)
print("He's %d centimeters tall." % my_height)
print("He's %d kilos heavy." % my_weight)
print("Actually he's not too heavy")
print("He's got %s eyes and %s hair." % (my_eyes, my_hair))
print('His teeth are usually %s depending on the coffee.' % my_teeth)

# this line is tricky, try to get it exactly right
print('If I add %d, %d, and %d I get %d.' % (
      my_age, my_height, my_weight, my_age + my_height + my_weight))

# Study Drills
# 1. Change all the variables so there isn't th my_ in front. Make sure you 
#    change the name everywhere, not just where you used = to set them.
# 2. Try more format characters. %r is a very useful one. It's like saying 
#    "print this no matter what".
# 3. Search onlne for all of the Python format characters.
# 4. Try write some variables that convert the centimeters and kilos to inches 
#    and pounds. Work out the math in Python.

# Personal Challenge
# 5. The decimal numbers are being omitted when running the program. Why is 
#    that happening? Make it show the decimal numbers.

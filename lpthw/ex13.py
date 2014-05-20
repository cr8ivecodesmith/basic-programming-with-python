# Exercise 13: Parameters, Unpacking, Variables

from sys import argv

script, first, second, third = argv

print('The script is called:', script)
print('Your first variable is:', first)
print('Your second variable is:', second)
print('Your third variable is:', third)


# Study Drills
# 1. Try giving fewer that three arguments to your script. See that error you 
#    get? See if you can explain it.
# 2. Write a script that has fewer arguments and one that has more. Make sure 
#    you give the unpacked variables good names.
# 3. Combine raw_input with argv to make a script that gets more input from a 
#    user.
# 4. Remember that modules give you features. Modules. Modules. Remember 
#    because we'll need it later.

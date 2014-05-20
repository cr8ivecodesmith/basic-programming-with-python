# Exercise 11: Asking questions

print('How old are you?', end=' ')
age = input()
print('How tall are you?', end=' ')
height = input()
print('How much do you weigh?', end=' ')
weight = input()

print("So you're %r old, %r tall and %r heavy." % (age, height, weight))

# Note
# Notice that we put an end=' ' after the string in the print command. This so 
# we can change the default way Python ends a print command from a newline (\n) 
# to just using a space (' ').

# Study Drills
# 1. Go online and find out what Python's input() does.
# 2. Can you find other ways to use it? Try some of samples you find.
# 3. Write another "form" like this to ask some other questions.

# Personal Challenge
# 4. Remove the end=' ' in the print command. What happens?

# Exercise 6: Strings and Text

x = 'There are %d types of people.' % 10
binary = 'binary'
do_not = "don't"
y = 'Those who know %s and those who %s' % (binary, do_not)

print(x)
print(y)

print('I said: %r.' % x)
print("I also said: '%s'." % y)

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print(joke_evaluation % hilarious)

w = 'This is the left side...'
e = 'a string with a right side.'

print(w + e)


# Study Drills
# 1. Go through this program and write a comment above each line explaining it. 
# 2. Find all the places where a string is put inside a string. There are 4 
#    places.
# 3. Are your sure there are only 4 places? How do you know?
# 4 Explain why adding two strings with w and e with + makes a longer string.

# Exercise 14: Prompting and Passing

from sys import argv

script, user_name = argv
prompt = '> '

print("Hi {}, I'm the {} script.".format(user_name, script))
print("I'd like to ask you a few questions.")
print('Do you like me {}?'.format(user_name))
likes = input(prompt)

print('Where do you live {}?'.format(user_name))
lives = input(prompt)

print('What kind of computer do you have?')
computer = input(prompt)

print("""
Alright, so you said {!r} about liking me.
You live in {!r}. Not sure where that is.
And you have a {!r} computer. Nice.
""".format(likes, lives, computer))


# Study Drills
# 1. Find out what Zork and Adventure were. Try to find a copy and play it.
# 2. Change the prompt variable to something else entirely.
# 3. Add another argument and use it in your script.
# 4. Make sure you understand how I combined a """ style multi-line string with 
#    the format command as the last print.

# Personal Challenge
# 6. Go online and find out more about the format command. Why would we prefer 
#    it over the usual way we format strings?
# 7. What does the {!r} formatter equivalent to?

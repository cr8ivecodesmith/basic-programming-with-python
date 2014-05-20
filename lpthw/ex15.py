# Exercise 15: Reading files

from sys import argv

script, filename = argv

txt = open(filename)

print("Here's your file {!r}:".format(filename))
print(txt.read())

print('Type the filename again:')
file_again = input('> ')

txt_again = open(file_again)

print(txt_again.read())


# Study Drills
# 1. Above each line write out what it does.
# 2. If you are not sure ask someone for help or search online. Many times
#    searching for "python THING" will find answers for what that THING does in
#    Python. Search for "python open".
# 3. The term "command" is interchangeably referred to "functions" and
#    "methods". Search online to see how to create one in Python.
# 4. Get rid of lines 12-17 and run the script again.
# 5. Run pydoc file and scroll down until you see the read() command
#    (method/function). See all the other ones you can use? Skip the ones that
#    have __ (two underscores) in front because those are junk. Try some of the
#    other commands.
# 6. Startup python again and use open from the prompt. Notice how you can open
#    files and run read on them right there?
# 7. Have your script also do a close() on the txt and txt_again variables.
#    It's important to close files when you are done with them.

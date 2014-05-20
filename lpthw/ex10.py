# Exercise 10: What was that?

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backlash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print(tabby_cat)
print(persian_cat)
print(backlash_cat)
print(fat_cat)

# Study Drills
# 1. Memorize all the escape sequences by putting them on flash cards.
# 2. Use ''' (triple single-quotes) instead. Can you see why you might use that 
#    instead of """?
# 3. Combine escape sequences and format strings to create a more complex 
#    format.
# 4. Remeber the %r format? Combine %r with double-quote and single-quote 
#    escapes and print them out. Compare %r with %s. Notice how %r prints it 
#    the way you'd write it in your file, but %s prints it the way you'd like 
#    to see it?

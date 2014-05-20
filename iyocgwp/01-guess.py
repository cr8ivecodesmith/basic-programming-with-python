"""
Invent Your Own Computer Games with Python - Chapter 4

Instructions:
- Copy the code below (type it!) and save it as "guess.py".
- Make sure the program runs.

Remember typing the code practices your attention to detail as
well as getting used to writing code.


Concepts:
- import statements
- modules
- arguments
- while statements
- conditions
- code blocks
- booleans
- comparison operators
- difference between = and ==
- if statements
- break keyword
- str() and int() functions
- random.randint() function

Optional task:
You may do an advanced review on the concepts above or read
the book on chapter 4.

After lecture task:
To review the concepts introduced in this program, read the
summary of chapter 4.

Write a note on each concept and explain them briefly in
your own words.
"""
# This is a guess the number game.
import random

guessesTaken = 0

print('Hello! What is your name?')
myName = input()

number = random.randint(1, 20)
print('Well, ' + myName + ', I am thinking of a number between 1 and 20.')

while guessesTaken < 6:

    print('Take a guess.')  # There are four spaces in front of print.

    guess = input()
    guess = int(guess)

    guessesTaken = guessesTaken + 1

    if guess < number:
        print('Your guess is too low.')  # There are eight spaces in front of print.

    if guess > number:
        print('Your guess is too high.')

    if guess == number:
        break

if guess == number:
    guessesTaken = str(guessesTaken)
    print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!')

if guess != number:
    number = str(number)
    print('Nope. The number I was thinking of was ' + number)


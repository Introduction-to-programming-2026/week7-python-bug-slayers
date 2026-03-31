# Project 2 — Number Guessing Game
# Author: your name here

import random

# TODO: generate a random secret number between 1 and 10

# TODO: set up a guesses counter

# TODO: get the user's first guess

# TODO: while loop — keep asking until the guess is correct
#   - print "Too low!" or "Too high!" on each wrong guess
#   - count each guess

# TODO: print the congratulations message with the number of guesses


# Project 2 — Number Guessing Game

import random

# secret number
secret = random.randint(1, 10)

# counter
guesses = 0

# first guess
guess = int(input("Guess a number between 1 and 10: "))

# loop
while guess != secret:
    guesses += 1

    if guess < secret:
        print("Too low!")
    else:
        print("Too high!")

    guess = int(input("Try again: "))

# correct guess
guesses += 1
print(f"Congratulations! You guessed it in {guesses} tries.")
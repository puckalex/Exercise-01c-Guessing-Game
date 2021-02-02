#!/usr/bin/env python3
import sys, random
assert sys.version_info >= (3,9), "This script requires at least Python 3.9"
number = random.randrange(1,101)
while(True):
    guess = input("Guess a whole number from 1 to 100: ")
    try:
        guess = int(guess)
    except:
        print("That wasn't a number! Try again!")
        continue
    if guess > number:
        print("Oops! Too high, try again!")
    elif guess < number:
        print("Oops! Too low, try again!")
    elif guess == number: 
        print("Great job! You got it!")
        break
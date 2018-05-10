# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 16:27:44 2018

@author: positiveoutlier

Guess the Number Game!
The user thinks of an integer between 0 (inclusive) and 100 (not inclusive). 
The computer makes guesses, and the user will give it input - is its guess too high or too low? 
Using bisection search, the computer will guess the user's secret number!
"""

low = 0
high = 100
hint = 'l'

print("Please think of a number between 0 and 100!")

while hint != 'c':
    average = int((low + high)/2)
    print("Is your secret number " + str(average) + "?")
    print("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.", end=' ') 
    hint = input()
    if hint == 'l':
        low = average
    elif hint == 'h':
        high = average
    elif hint == 'c':
        print("Game over. Your secret number was: " + str(average))
        break
    else:
        print("Sorry, I did not understand your input.")
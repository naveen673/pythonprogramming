# Author : Naveen Reddy
# Date : 28/08/2021
# Version : 1.0

# Guess the random number game
# one player vs the computer

import random # random is an inbuilt package in Python, it will fetch random variable values
minGuess = 1
maxGuess = 6

# Ask the user for their name and their guess
name = input("What is your name? ")
print("Hi",name)
print("Enter a number between: " + str(minGuess) + " and " + str(maxGuess))
guess = int(input("What is your guess? "))

# Generate a random number and tell the user if they won or lost
secretNumber = random.randint(minGuess, maxGuess)
if(guess == secretNumber):
    print("Congratulations, you got it right!")
else:
    print("You lose - The number was ", secretNumber)

print("Thank you for playing Guess the Number.")
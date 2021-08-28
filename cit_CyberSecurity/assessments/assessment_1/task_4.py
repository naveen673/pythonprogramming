'''
Write a python script that will ask a user two questions-
what year he was born and if he already had his birthday this year.
The answer to the first question will be a year (e.g., 1992,
and the answer to the second question will be either “yes” or “no”.
Then, based on these answers, print the user’s correct age on the screen, and wish him a birthday message.
If his birthday is celebrated already, print “I am sure that was a good day!”.
If it is in the future, print “I hope you will have a good one!”
'''

question1 = int(input("What year you were born?: "))

if question1 < 2021:
    print(question1)

question2 = input("Is your birthday gone for this year?: ")

if question2 == 'Yes' or question2 == 'yes':
    print("You are " + str(2021-question1) + " years old.")
    print("I am sure that was a good day!")
else:
    print("You are " + str(2021 - question1-1) + " years old.")
    print("I hope your will have a good one!")
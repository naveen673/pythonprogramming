'''
This program is nearly complete:


a.     Line 4 and line 6 need some code added. Can you complete the program?
b.    Can you change the program to add numbers with decimals as well? (hint: while int() converts a value to an integer, float() works with numbers that have decimals)
c.     Can you add a line to the program that will print the running total? (e.g. “The sum is now 5. The sum is now 7.”)

'''

print("This program adds numbers.")
userInput = 'y'
sum = 0
while(userInput == 'y'):
    # number=int(input("Enter a number: "))
    number = float(input("Enter a number: "))  # to add numbers with decimals as well
    sum = sum + number
    print("The sum is now ", sum)  # to print “The sum is now 5. The sum is now 7.”)
    userInput = input("Would you like to add another number?")
print("The sum of those numbers is: "+str(sum))

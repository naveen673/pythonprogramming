'''
Task 2

Write a function named collatz() that has one parameter named number. If number is even, then collatz() should print (number // 2) and return this value. If number is odd, then collatz() should print and return (3 * number + 1).
Then write a program that lets the user type in an integer and that keeps calling collatz() on that number until the function returns the value 1*.

*Amazingly enough, this sequence actually works for any integer—sooner or later, using this sequence, you’ll arrive at 1! Even mathematicians aren’t sure why. Your program is exploring what’s called the Collatz sequence, sometimes called “the simplest impossible math problem.”)- Source: Automate Boring Stuff with Python

'''
def collatz(a):
    if(a%2==0):
        print(a//2) # // means Floor Division example:15/2 will return 7 and not 7.5 .... Floor Division // will rounds the result down to the nearest whole number.
        return a//2
    else:
        print(3*a+1)
        return 3*a+1

while(True):
    a=int(input("Enter a whole number: "))
    value=collatz(a)
    if(value==1):
        break
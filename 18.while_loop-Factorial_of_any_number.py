'''
Factorial of any number n is represented by n! and is equal to 1*2*3*....*(n-1)*n. E.g.-
4! = 1*2*3*4 = 24
3! = 3*2*1 = 6
2! = 2*1 = 2
Also,
1! = 1
0! = 1
Write a program to calculate factorial of a number.
'''
'''
n=int(input("Enter a factorial number: "))
fac=1
number=n
if(n==0):
    print("The factorial of " + str(number) + " is 1")
else:
    while(n>=1):     #(n>0) gives the same result
        fac=fac * n
        n=n-1
    print("The factorial of " + str(number) + " is " + str(fac))
'''


n=int(input("Enter a factorial number: "))
fac=1
i=1
if(n==0):
    print("The factorial of " + str(n) + " is 1")
else:
    while(i<=n):     #(n>0) gives the same result
        fac=fac * i
        i=i+1
    print("The factorial of " + str(n) + " is " + str(fac))
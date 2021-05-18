'''
Create a function that determine if positive integer number is a prime number or not.

REMEBER:
A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
'''

# Program to check if a number is prime or not

# num = 15

# To take input from the user
#num = int(input("Enter a number: "))

# define a flag variable


# prime numbers are greater than 1
def is_prime(num):
    flag = False
    if num > 1:
        # check for factors
        for i in range(2, num):
            if (num % i) == 0:
                # if factor is found, set flag to True
                flag = True
                print(i)
                # break out of loop
                #break

    # check if flag is True
    if flag:
        print(num, "is not a prime number")
    else:
        print(num, "is a prime number")

a=int(input("enter a numbet to check prime or not:\n"))
is_prime(a)
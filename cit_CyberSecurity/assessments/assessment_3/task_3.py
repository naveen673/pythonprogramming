'''
Task 3
# Write a python program to find the factors of a given number.
# The factors of a number are those, which are divisible by the number itself and 1.
# For example, the factors of 15 are 1, 3, 5.
# Please follow the below steps to complete this task:
# Define a function which will take the number as parameter and perform the task.
# Use for loops and if expression to perform the factorization.

# Python Program to find the factors of a number

# This function computes the factor of the argument passed
'''

def print_factors(x):
   print("The factors of",x,"are:")
   for i in range(1, x + 1):
       if x % i == 0:
           print(i)

num = int(input("Enter the number to find it's factors: "))

print_factors(num)
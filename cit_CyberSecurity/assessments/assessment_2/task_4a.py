
"""
a) Write a simple python script to print a times table. Please print the times table for a range of numbers. Please follow the below steps to write the script.
i. Please take input from the user for producing the multiplication table.
ii. You as a user will provide two numbers, one for the minimum and other for the maximum. The range between minimum and maximum is expected not to exceed the value 10. For example, minimum = 5, and maximum = 10.
iii. For this, use for loop to calculate the times table for the given numbers.
iv. Please consider the below output as an example.
"""
"""
--- psuedo code ---

Take the three inputs multiplication table number, min value and max value for the range of the table
for value in range(minvalue, maxvalue+1):
   print the multiplication pattern (number x value = number*value)
"""


# Multiplication table (from 1 to 10) in Python

num = int(input("Display multiplication table of?: "))
min=int(input("Enter the min range of table to start: "))
max=int(input("Enter the max range of table to finish: "))

for i in range(min, max+1):
   print(num, 'x', i, '=', num*i)




"""
Write a python script to print and determine the summation of odd numbers within a given range.
Use a for loop ranging from lower to upper limit, and then use an if statement to check which
are odd numbers for printing and calculating the summation.
"""

"""
--- psuedo code ---

take two inputs from user lower and upper for number range
initialize sum variable to zero to calculate the sum of odd numbers.
for i in range(lower to upper+1):
   if i%2!=0 then
       print the number and say it is odd number
       sum=sum+i
print(sum of all odd numbers)
"""


lower=int(input("Enter the lower limit for the range: "))
upper=int(input("Enter the upper limit for the range: "))
sum=0
for i in range(lower,upper+1):
    if(i%2!=0):
        print("the odd number is ", i)
        sum=sum+i
print("the summation of odd numbers is ", sum)

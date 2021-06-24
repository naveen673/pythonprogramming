'''
Write a program to check if a year is leap year or not.
If a year is divisible by 4 then it is leap year but if the year is century year like 2000, 1900, 2100 then it must be divisible by 400.
'''
# 0 is False and 1 is True

year=int(input("Enter the year in yyyy format: "))

if(year%400==0):
    print("The year " + str(year) + " is a Leap Year and a century year.")
elif(year%4==0):
    print("The year " + str(year) + " is a Leap Year.")
else:
    print("The year " + str(year) + " is not a Leap Year.")



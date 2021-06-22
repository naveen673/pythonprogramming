# A company decided to give bonus of 5% to employee, if his/her year of service is more than 5 years.
# Ask user for the salary and year of service then print the net bonus.

salary=float(input("The the salary of the Employee: "))
yos=int(input("Enter the completed number of years of service: "))

if(yos>5):
    #bonus=salary*0.05
    bonus=(5/100)*salary
    print("The bonus for number of years served is ", bonus)
else:
    print("The Employee is not eligible for bonus")
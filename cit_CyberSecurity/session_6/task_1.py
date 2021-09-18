'''
Task 1
You are working in the HR department of a factory and they have asked you to create a program to calculate gross pay of the workers based on hours worked and hourly rate of pay. Your program will take “Hours” and “Rate” as inputs and display the gross pay as output. Take into consideration that workers are paid 1.5 times the hourly rate for the hours worked above 40 hours.
Write the program by using a function named salarycalculator that takes hours and rate as input and returns payment as output.
Sample Executions:
Enter Hours: 30						Enter Hours: 45
Enter Rate: 10						Enter Rate: 10
Pay: $300.0						Pay: $475.0

'''

def salarycalculator(hours, rate):
    pay=0
    if(hours>40):
        overtime=hours-40
        pay=(40*rate)+(overtime*rate*1.5)
    else:
        pay=hours*rate
    return pay

hours=float(input("Enter the number of hours worked: "))
rate=float(input("Enter the rate per hour: "))

grosspay=salarycalculator(hours, rate)
print("Salary for the hours worked is ",grosspay)
'''
2.	Write an if/elif statement that assigns a value to the variable bonus depending on the amount of sales.
Assume the amount of the sales is stored in a variable called sales.
'''

sales=int(input("Enter the amount of product sales: "))
bonus=0
if sales>=100000:
    bonus=10000
elif sales>=75000:
    bonus=5000
elif sales>=50000:
    bonus=2500
else:
    bonus=1000
print("Bonus for the product sales is: ", bonus)
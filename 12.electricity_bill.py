'''
Write a program to calculate the electricity bill (accept number of unit from user) according to the following criteria :
             Unit                                                     Price
First 100 units                                               no charge
Next 100 units                                              Rs 5 per unit
After 200 units                                             Rs 10 per unit
(For example if input unit is 350 than total bill amount is Rs2000)
'''

units=int(input("The number of units consumed: "))
if(units<101):
    price=0
    print("Electricity bill is: $",price)
elif(units>100 and units<201):
    price=(units-100)*5
    print("Electricity bill is: $",price)
elif(units>200):
    price=(units-200)*10+500
    print("Electricity bill is: $",price)
else:
    print("Electricity bill is invalid")
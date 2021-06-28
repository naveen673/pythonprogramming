'''
Take integer inputs from user until he/she presses q (Ask to press q to quit after every integer input).
Print average and product of all numbers.
'''

i=0
sum=0
product=1
choice="Y"
while(choice!="Q" and choice!="q"):
    n=int(input("Enter an integer: "))
    product=product*n
    sum=sum+n
    choice=input("Press Q to quit from the loop: ")
    i=i+1
print(i)
average=sum/i
print(average)
print(product)
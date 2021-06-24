'''
Take 10 integers from keyboard using loop and print there average value on there screen.
'''

i=2
sum=0
while(i<21):
    a=int(input("Enter any valid integer: "))
    sum=sum+a
    print(a)
    i=i+2
print("The sum of 10 integers is ", sum)
print("The average of 10 integers is ", sum/10)
'''
Convert Fahrenheit to Celsius
f = float(input ("Degree in Fahrenheit:\t"))
c = (f-32)*(5.0/9.0)
print(c)
'''
'''

#If and Elseif statements.
# try:
a = int(input("First Number: \n")) #
b = int(input("Second Number: \n"))
c = int(input("Third Number: \n"))
if((a>b) and (a>c)):
    print(a)
elif((b>a) and (b>c)):
    print(b)
elif((a==b) or (b==c)):
    print("Input Error")
else:
    print(c)
# except:
#     print("Input error")

print("yes")

#For Loops
sum=0
n = int(input("Enter the number for range: \n"))
for i in range(n+1):
    # print("--first step----")
    # print(i)
    # print(sum)
    # print("---second step---")
    sum=sum+i
print(sum)
'''
'''
#Find the last digit of the entered number

a=int(input("Enter a number: "))
print(a%10)

#Find the number whether it is positive or negative for a 5 times
for i in range(0,5):
    num=float(input("Enter a number: "))
    if(num>0):
        print("The number is positive")
    elif(num<0):
        print("The number is negative")
    else:
        print("The number is zero")
'''
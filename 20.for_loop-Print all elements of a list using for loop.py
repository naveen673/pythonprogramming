'''
Print all elements of a list using for loop.
'''

# sports=[1,'cricket'] #sports is List, and [,,,,,] is Elements.
# for i in sports: #i is a variable and it represents Iterator (Instead of i we can give any variable).
#     print(i)

'''
Take 10 integers from user and add print sum of their squares 
'''

sum=0
for i in range(10):
    n=int(input("Enter an integer: "))
    print(n**2)
    sum=sum+(n**2)           # ** means Exponent in Python
print(sum)
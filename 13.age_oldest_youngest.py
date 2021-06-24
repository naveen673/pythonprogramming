# Ctrl + R is used to for replacement of any character/s.
'''
Take input of age of 3 people by user and determine oldest and youngest among them.
'''
age1=int(input("Enter the age of person 1: "))
age2=int(input("Enter the age of person 2: "))
age3=int(input("Enter the age of person 3: "))

def age_older(a,b,c):
    if (a > b and a > c):
        print("Person 1 is OLDER than person 2 and person 3 and the age is ", a)
    elif (b > a and b > c):
        print("Person 2 is OLDER than person 1 and person 3 and the age is ", b)
    elif (c > a and c > b):
        print("Person 3 is OLDER than person 1 and person 2 and the age is ", c)
    else:
        print("The age entered is invalid")
        
def age_younger(a,b,c):
    if (a < b and a < c):
        print("Person 1 is YOUNGER than person 2 and person 3 and the age is ", a)
    elif (b < a and b < c):
        print("Person 2 is YOUNGER than person 1 and person 3 and the age is ", b)
    elif (c < a and c < b):
        print("Person 3 is YOUNGER than person 1 and person 2 and the age is ", c)
    else:
        print("The age entered is invalid")
        
age_older(age1, age2, age3)
age_younger(age1, age2, age3)
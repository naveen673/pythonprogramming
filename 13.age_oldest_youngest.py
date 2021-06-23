'''
Take input of age of 3 people by user and determine oldest and youngest among them.
'''

age1=int(input("Enter the age of person 1: "))
age2=int(input("Enter the age of person 2: "))
age3=int(input("Enter the age of person 3: "))

if(age1>age2 and age1>age3):
    print("Person 1 is OLDER than person 2 and person 3 and the age is ",age1)
    #if(age1<age2 and age1<age2):
        #print("Person 1 is YOUNGER than person 2 and person 3 and the age is ",age1)
elif(age2>age1 and age2>age3):
    print("Person 2 is OLDER than person 1 and person 3 and the age is ",age2)
    #if(age2<age1 and age2<age3):
        #print("Person 2 is YOUNGER than person 1 and person 3 and the age is ",age2)
elif(age3>age1 and age3>age2):
    print("Person 3 is OLDER than person 1 and person 2 and the age is ",age3)
    #if(age3<age1 and age3<age2):
        #print("Person 3 is YOUNGER than person 1 and person 2 and the age is ",age3)
else:
    print("The age entered is invalid")

'''
Task 2:
A. Define a function which can generate a list where the values are square of numbers
between 1 and 20 (both included). Then the function needs to print the first 5 elements
in the list
'''
def printValues():
    l = list()
    for i in range(1, 21):
        l.append(i ** 2)
    print(l[:5])


printValues()


'''
Task 2:
B. Define a function that can accept two strings as input and print the string with maximum
length in console. If two strings have the same length, then the function should print
all strings line by line.
'''
def printVal(s1,s2):
    len1 = len(s1)
    len2 = len(s2)
    if len1 > len2:
        print(s1)
    elif len1 < len2:
        print(s2)
    else:
        print(s1)
        print(s2)

s1,s2=input().split()
printVal(s1,s2)
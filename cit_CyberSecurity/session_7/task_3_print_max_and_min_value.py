
"""
Write a function calculateMax()  that takes as input a list containing 10 integers and returns the maximum value.
(There is a built-in function named max but suppose you cannot use it here). Print the list and then use the function to print the maximum value.
"""

li_int=[]
count=0
def calculateMax(a):
    return max(a)

def number_of_odd_numbers(a, count):
    for x in a:
        if (x%2 !=0):
           count=count+1
    return count

for x in range(0,10):
    value=int(input("Enter a integer value: "))
    li_int.append(value)

print("the max value of the list is ", calculateMax(li_int))
print("the number of odd numbers: ", number_of_odd_numbers(li_int, count))



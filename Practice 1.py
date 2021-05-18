#Practice 1: Take 10 integers from keyboard using loop and print their average value on the screen.

#For Loops
# sum=0
# n = int(input("Enter the number for range: \n"))
# for i in range(n):
#     print(sum)
#     i=10
#     sum=sum+i
# print(sum)
# a = float(sum/i) #to find average
# print(a)


sum=0
for i in range(10):
    n = int(input("Enter the number for range: \n"))
    sum=sum+n
average=sum/10
print(average)
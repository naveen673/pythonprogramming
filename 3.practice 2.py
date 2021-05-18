#Practice 2: Print multiplication table of 24, 50 and 29 using loop.
sum=0
# n = int(input("Enter the number for range: \n"))
# for i in range(n):
#     print(sum)
#     m=24
#     sum=sum+m
# print(sum)
t_val=0
t_num=int(input("Enter the table number: \n"))
t_range=int(input("Enter the number for table range: \n"))
for i in range(t_range):
    t_val=t_num*i
    print(str(t_num)+"*"+str(i)+"="+str(t_val))



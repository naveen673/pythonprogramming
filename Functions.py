# def add(a,b):
#     c=a+b
#     return c
# def add(a,b):
#     return a+b
# #add()
#
# def sub(a,b):
#     c=a-b
#     return c
#
# def multi(a,b):
#     c=a*b
#     return c
#
# def div(a,b):
#     c=a/b
#     return c
#
#
# a = float(input("Enter the first number: \n"))
# b = float(input("Enter the second number: \n"))
#
# t_add_val=add(a,b)
# print("The sum of two numbers: " + str(t_add_val))
#
# t_sub_val=sub(a,b)
# print("The subtraction of two numbers: ", t_sub_val)
#
# t_multi_val=multi(a,b)
# print("The multiplication of two numbers ", t_multi_val)
#
# t_div_val=div(a,b)
# print("The division of two number " + str(t_div_val))

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def div(a,b):
    return a/b
def multi(a,b):
    return a*b

a = float(input("Enter the first number: \n"))
b = float(input("Enter the second number: \n"))
print("The sum of two number: ", add(a,b))
print("The subtraction of two number: ", sub(a,b))
print("The division of two number: ", div(a,b))
print("The multiplication of two number: ", multi(a,b))
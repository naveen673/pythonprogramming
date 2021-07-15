'''
Write function select_unique_values to get unique values from a list.
Note: result should be in a list.
'''

def select_unique_values(a):
    number=set(a)
    unique_list=list(number)
    return unique_list

result=select_unique_values([2,2,2,3,3,1,2,6,7,8,9,9,10])
print(result)
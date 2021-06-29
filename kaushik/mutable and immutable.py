'''
Mutable - object can be changed. eg- list
immutable - object cannot be changed. eg - tuple
tuple is represented as ( , )
list is represented as [ , ]
'''
# t=(10, 11)
# for value in t:
#     print(value)
'''
t[0]=1    gives an error as tuple is immutable
error is TypeError: 'tuple' object does not support item assignment
'''

# l=[20, 15]
# for value in l:
#     print(value)
# l[0]=30
# l[1]=45
# print(l)

# Tuple Methods: Tuple is predefined class which has functions. any function is called by writing object.methodname
t=(1,4,5,8,5,9,5,5) # defined a tuple , where t is called tuple object
# let's count the number 5 how many times in the defined tuple
# for this we use pre defined tuple method count
print(t.count(5))
# index is another method which gives the position of the element in the tuple.
print(t.index(9))

'''
List Slicing
'''
m=[45,12,25,48,6]
print(m[0:4])
# Result of above equation is called Sub List of List 'm' this is known as List Slicing.

"""
If you want access to the index of each element within the body of a loop, 
use the built-in enumerate function
"""
animals=['cat', 'dog', 'monkey']
for idx, animal in enumerate(animals):
    print(str(idx)+') ' +animal)

'''
list method insert
insert a number 10 at index 2
'''
l=[2,4,20,30]
l.insert(2, 10)
print(l)




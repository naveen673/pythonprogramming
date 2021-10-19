'''
Task 1:
A. Write a script that will print the following list after removing all the duplicate items.
li=[12,24,35,24,88,120,155,88,120,155]
'''


li=[12,24,35,24,88,120,155,88,120,155]

dup_items = set()
uniq_items = []
for x in li:
    if x not in dup_items:
        uniq_items.append(x)
        dup_items.add(x)

print(uniq_items)


'''
Task 1:
B. Write a script that will remove the 0th, 4th and 5th numbers form the above list.
Hints:-> Use list comprehension to delete a bunch of element form the list and use enumerate() to get (index, value) tuple.
'''

li = [x for (i,x) in enumerate(li) if i not in (0,4,5)]
print(li)
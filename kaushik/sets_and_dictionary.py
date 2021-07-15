animals={'dog', 'cat', 'dog', 'monkey', 'tiger', 'lion'}
print(animals)
a=set("12345")
b=set("34567")
print(a)
print(b)
print(a-b) # letters in a but not in b- {'2', '1'}
print(b-a) # letters in b but not in a - {'6', '7'}
print(a|b) # letters in a or b or both - {'4', '5', '2', '3', '1', '7', '6'}
print(a&b) # letters in both a and b - {'5', '3', '4'}
print(a^b) # letters in a and b but not both - {'2', '7', '1', '6'}

# two type of dictionaries
key_list=['sports']
d={'animal':'dog', 'fruit':'mango'}
# d={'animals':['dog', 'cat'], 'fruits':['apple', 'mango']} # value for key is declared in list.
print(d)
print(d.keys())
print(d.values())
for key in d.keys():
    key_list.append(key)
print(key_list)

#convert set to list
animals_list=list(animals)
print(animals_list)
# convert list to set
category_set = set(key_list)
print(category_set)

a=[1,2,3,3, 4,5]
b=set(a)
c=list(b)
print(c)
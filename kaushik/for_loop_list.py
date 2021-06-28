# fruits=['banana', 'mango', 'strawberry', 'apple']
# for fruit in fruits:
#     print(fruit)

integers=[1, 2] #list
for i in range(5):
    integer=int(input("enter the integer to store: "))
    integers.append(integer) #append means adding a new item to the existing list at the back of the last item, it increases the list size with no limit

print(integers)
print(len(integers))
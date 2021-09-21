
"""
From given list below
gadgets = [“Mobile”, “Laptop”, 100, “Router”, 310.28, “server pods”, 27.00,“jacks”, 1000, “Laptop Case”, “Camera Lens”]

a) create separate lists of strings and numbers.

b) Sort the strings list in ascending order

c) Sort the strings list in descending order

d) Sort the number list from lowest to highest

e) Sort the number list from highest to lowest
"""
gadgets_str=[]
gadgets_int=[]
gadgets = ["Mobile", "Laptop", 100, "Router", 310.28, "server pods", 27.00,"jacks", 1000, "Laptop Case", "Camera Lens"]
for x in gadgets:
    if isinstance(x, int) or isinstance(x, float):
        gadgets_int.append(x)
    else:
        gadgets_str.append(x)

print(gadgets_str, gadgets_int)


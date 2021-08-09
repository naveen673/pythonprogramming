'''
Scenario
Convert the expressions provided below (lines 4, 8, 12, and 16 under Testing code section) into expressions that contain shortcut operators. Type the converted expressions in lines 5, 9, 13, and 17 respectively.
Run your code each time you convert a single expression, and check if the outputted results match the expected output.

Testing code
1.	x = 15
2.	y = 8
3.
4.	# the shorthand of x = x + y:
5.	# enter the expression with a shortcut operator here
6.	print(x)
7.
8.	# the shorthand of x = x - y:
9.	# enter the expression with a shortcut operator here
10.	print(x)
11.
12.	# the shorthand of x = x % y:
13.	# enter the expression with a shortcut operator here
14.	print(x)
15.
16.	# the shorthand of y = y ** y:
17.	# enter the expression with a shortcut operator here
18.	print(y)

Expected Output
23
15
7
16777216
'''

x=15
y=8

# the shorthand of x = x + y:
x+=y
print(x)

# the shorthand of x = x - y:
x-=y
print(x)

# the shorthand of x = x % y:
x%=y
print(x)

# the shorthand of y = y ** y:
y**=y
print(y)
'''
Print the following patterns using loop:
*
**
***
****
'''
'''
i=1
symbol="*"
while(i<5):
    print(str(symbol)*i)
    i=i+1
'''
'''
  *
 ***
*****
 ***
  *
'''
'''
i=1
k=2
symbol="*"
while(i<6):
    print(" " * k + str(symbol)*i)# + " " *k)
    i=i+2
    k=k-1

i=3
k=1
while(i>0):
    print(" " * k + str(symbol)*i)
    i=i-2
    k=k+1
'''
'''
1010101
 10101
  101
   1
'''
i=3
k=0
symbol="10"

while(i>=0):
    print(" " * k + symbol * i + "1")
    i=i-1
    k=k+1
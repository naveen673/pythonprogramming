"""
Consider the following scenario to write a python script using while loop.
Listen to our story: a boy and his father, a computer programmer, are playing with wooden blocks. They are building a pyramid. Their pyramid is a bit weird, as it is actually a pyramid-shaped wall - it's flat. The pyramid is stacked according to one simple principle: each lower layer contains one block more than the layer above.

Your task is to write a program which reads the number of blocks the builders have, and outputs the height of the pyramid that can be built using these blocks.
Note: the height is measured by the number of fully completed layers - if the builders don't have a sufficient number of blocks and cannot complete the next layer, they finish their work immediately.
Test the code using the test case provided below.
Sample Input: 6  Corresponding output: Height of the pyramid is 3
Sample Input: 20  Corresponding output: Height of the pyramid is 5
Sample Input: 1000  Corresponding output: Height of the pyramid is 44
Sample Input: 2  Corresponding output: Height of the pyramid is 1
"""
'''
---- psuedo code ---

initialize height and inlayer to be zero and 1 respectively
take the number of blocks from user
while (inlayer is less than or equal to number of blocks):
   height=height+1
   blocks=blocks-inlayer
   inlayer=inlayer=inlayer+1
'''

blocks = int(input("Enter the number of blocks: "))

height = 0

inlayer = 1

while inlayer <= blocks:

    height += 1
    blocks -= inlayer
    inlayer += 1

print("The height of the pyramid: ", height)


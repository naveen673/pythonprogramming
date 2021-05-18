# Write a program that prints the numbers from 1 to 100. But for multiples of three print
# “Fizz” instead of the number and for the multiples of five print “Buzz”.
# For numbers which are multiples of both three and five print “FizzBuzz”

#% percentage sign is called as Modulous Operator

for i in range(1,101):    #we give 1 here to start the loop from number 1, instead 0.
    if(i%3==0 and i%5==0):
        print("FizzBuzz")
    elif(i%5==0):
        print("Buzz")
    elif(i%3==0):
        print("Fizz")
    else:
        print("The number is not multiple of 3 or 5")

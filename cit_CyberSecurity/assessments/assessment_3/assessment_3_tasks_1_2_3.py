'''
Task 1
The cyber security department for Blooming Cafe wants to know the temperature of Canberra in immutable list for a specific purpose. They have certain criterions to solve this problem. The criterions are given below:
SL NO	Requirement Specification
1	Provide an option where they can take temperature in either Fahrenheit or Celsius scale
2	Need to collect five temperature from user and add them to the immutable list
3	Convert the temperature from the Celsius to Fahrenheit or vice versa
4	Delete the last value. You can convert the tuple to list to do this.
5	Display the result in tuple
The Conversion Formula for Fahrenheit to Celsius is given below:
T(°C) = (T(°F)  - 32) × 5/9  Here T(°C)  refers to the temperature in Celsius and T(°F)  is defined for Fahrenheit temperature.
The Conversion formula for Celsius to Fahrenheit is given below:
T(°F) = T(°C) × 9/5 + 32 Here T(°C)  refers to the temperature in Celsius and T(°F)  is defined for Fahrenheit temperature.
'''
temp=()
degree=input("Enter the type of scale you are using to measure temperature - F/C: ")
for i in range(0,5):
    temperature=float(input("Enter the temperature: "))
    if(degree=='F' or degree=='f'):
        temp_C=(temperature-32)*5/9
        temp=temp+(temp_C,)
    else:
        temp_F=(temperature*(9/5))+32
        temp=temp+(temp_F,)

list_temp=list(temp)
list_temp.pop(4)
print(tuple(list_temp))


'''
Task 2
# Write a python program to find the factors of a given number.
# The factors of a number are those, which are divisible by the number itself and 1.
# For example, the factors of 15 are 1, 3, 5.
# Please follow the below steps to complete this task:
# Define a function which will take the number as parameter and perform the task.
# Use for loops and if expression to perform the factorization.

# Python Program to find the factors of a number

# This function computes the factor of the argument passed
'''

def print_factors(x):
   print("The factors of",x,"are:")
   for i in range(1, x + 1):
       if x % i == 0:
           print(i)

num = int(input("Enter the number to find it's factors"))

print_factors(num)


'''
Task 3 Widget
'''


def main():
    print(" ")
    print("=========================================================")
    print("Main Menu. Choose one of the options as 1, 2, 3, 4, 5: ")
    print("1. Enter Personal Data")
    print("2. Salary Calculator")
    print("3. Gadget Inventory")
    print("4. Gadget Cost Calculator")
    print("5. Exit")
    option = int(input("Choose an option to proceed: "))
    if option == 1:
        personalData()
    elif option == 2:
        salaryCalculator()
    elif option == 3:
        gadgetInventory()
    elif option == 4:
        gadgetsCostCalculator()
    elif option == 5:
        print("Exited the program")
    else:
        print("Incorrect selection")
        main()

def personalData():
    global emp
    keys=['Name','Phone','Designation']
    for i in range (0, 3):
        values=[]
        name = input("Enter the name of cyber security expert: ")
        values.insert(i, name)
        phone = int(input("Enter the phone number of employee: "))
        values.insert(i+1, phone)
        designation = input("Enter the designation of employee: ")
        values.insert(i+2, designation)
        emp.insert(i,values)
        print("_________________________________________________")
        print(" ")
    print("Details of all employees below: ")
    for j in range (0, 3):
        print(dict(zip(keys,emp[j])))
    main()

def salaryCalculator():
    name = input("Enter employee name: ")
    wage = int(input("Enter wage per hour: "))
    hours = int(input("Enter hours worked by employee: "))
    totalSalary = wage * hours
    print("----------------------------------")
    print("Total Salary of " + name + " is: ", totalSalary)
    main()

def gadgetInventory():
    print("Gadget Inventory")
    global routers
    global switches
    global laptops
    global mainframe
    print("Inventory: Routers: ", routers, ", Switches: ", switches, ", Laptops: ", laptops, ",Mainframe: ",mainframe)
    print(" ")
    choice = input("What do you want to add? Press “R” for router, “S” for switch, “L” forLaptop, “M” for Mainframe: ")
    if choice == "r" or choice == "R":
        addRouters = int(input("How many routers do you want to add: "))
        routers = routers + addRouters
    elif choice == "s" or choice == "S":
        addSwitches = int(input("How many switches do you want to add: "))
        switches = switches + addSwitches
    elif choice == "l" or choice == "L":
        addLaptops = int(input("How many laptops do you want to add: "))
        laptops = laptops + addLaptops
    elif choice == "m" or choice == "M":
        addMainframe = int(input("How many mainframe do you want to add: "))
        mainframe = mainframe + addMainframe
    else:
        print(" ")
        print("Invalid choice")
        gadgetInventory()

    print(" ")
    print("Gadget Inventory Updated. Inventory: Routers: ", routers, ", Switches: ", switches, ",Laptops: ",laptops,", Mainframe: ",mainframe)
    main()

def gadgetsCostCalculator():
    print("Gadgets Cost Calculator")
    item = input("Enter the item name to calculate price: ")
    price = int(input("Enter the price of the item: "))
    noOfItems = int(input("Number of items required: "))
    print("Total price of", item, ":", price * noOfItems)
    print(" ")
    main()



emp = []
routers = 3
switches = 2
laptops = 16
mainframe = 1
main()
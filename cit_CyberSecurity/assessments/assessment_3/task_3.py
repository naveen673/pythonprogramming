
'''
Task 3 Widget

Scenario:
WIDGET is a small accounting company based in Belconnen ACT.  They have 15 employees, including an Office Manager and the Business Owner. Ten of the employees work onsite at the office, whilst the remaining five work remotely from home or at a client’s premises.  Responsibility for ICT resides with their Office Manager, who is working their way through a TAFE ICT course in their spare time. WIDGET’s ICT Infrastructure consists of the following:
•	All the staff use laptops with Windows 10 Pro as the SOE.  These are all standard licenses, are patched and do NOT have security software installed.  Staff are free to choose their own passwords for their individual machines.
•	The business has recently moved to the Office 365 Business subscription service for Microsoft Office applications.
•	Wireless internet access for office staff is provided via ADSL using a D-Link-2740B wireless router and the Wi-Fi password is publicly available. Staff are permitted to connect their mobiles, laptops and other electronic devices through this wireless network. They also can form an internet-of-things structure by connecting these devices at the same time for work purposes.
•	Wired network and internet access is also provided by a recently installed NETGEAR JGS524 24-Port Gigabit Switch.  There are 20 network jacks available, which can be used to connect any physical computing devices. Couple of jacks are located in the public area of the office accessible to clients and visitors.
•	Staff working remotely use either their personal mobile phones as hot spots or their home internet connections to connect to the internet, and they do not have any password policy enforced.
•	Sensitive data is stored on laptops, servers and the NAS without using cryptographic techniques.
•	Employees share passwords and logins with each other if they are having difficulty logging in or they need to access to material on other machines.
The business does not have a website and instead conduct marketing campaigns through a Facebook page and a Twitter account. The user name and password for these services are the same as the Business Owner’s username and password for his work laptop.

Task instructions:
There are some security holes in the organisation and it is the responsibility of the security experts to fix these. However, you are hired as a python programmer for this organization, and you have been asked to create a simple inventory management system for the company. You have to prepare a console from which the company can manage the costing of different gadgets and the cyber professionals hired. The console will have the following options:
1.	Enter Personal Data:
•	You should be able to add name, phone number and designation of the hired cyber professionals.
•	You must save the details entered from the prompt and then display it back to the screen.
•	Perform the task for at least 3 employees.  Display the information in any systematic manner. It can be done by using list, tuple, file operation or dictionary.
2.	Salary Calculator
•	Your program should be able to take as input hourly wage and total hours worked, and then print the total salary for the month considering the employees taken as input.
3.	Gadget Inventory
•	Your program should be able to show the current status of the inventory for each gadget (Router, Switch, Laptop, Mainframe) and update these numbers as entered by the user. Sample input/output:


Inventory: 3 Routers, 2 Switches, 16 Laptops, 1 Mainframe
What do you want to add? Press “R” for router, “S” for switch, “L” for Laptop, “M” for Mainframe.
>>> R
>> How many routers do you want to add?
>>> 2
>>> Gadget Inventory Updated. Inventory: 5 Routers, 2 Switches, 16 Laptops, 1 Mainframe
4.	Gadgets Cost Calculator
•	Your program should be able to take as input the price of an item and the number of items needed, and print the total cost.
5.	Exit
•	Choosing this option will end the program.

You can follow the below steps to complete this task:
•	Create a menu using if-else for the mentioned options.
•	Use a function called main () within which this menu will be declared.
•	Define functions for each of these options. The options will work once the correct number is entered through if-else statement.
•	Call main() at the end of these functions so that the main menu is shown after each of  the operations (unless it is “Exit”).
•	Use lists to save the data. You may need “list of lists” but how you design the program is up to you.
•	Provide inline comments wherever necessary.
•	Create a small user manual program for this task.

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
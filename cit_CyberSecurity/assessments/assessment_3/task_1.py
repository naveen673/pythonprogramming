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
degree=input("Enter the type of scale you are using to measure temperature as F/C: ")
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
print("The temperature is: " ,tuple(list_temp))
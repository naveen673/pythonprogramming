# Ask the user for the day, month, and year and displaye it in the following fashion dd/mm/yyyy

day=int(input("Enter the calendar day: "))
month=int(input("Enter the calendar month: "))
year=int(input("Enter the calendar year: "))

print(str(day)+ "/" + str(month)+ "/" +str(year))
print("%d/%d/%d" %(day,month,year))
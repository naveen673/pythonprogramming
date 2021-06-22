'''
A school has following rules for grading system:
a. Below 25 - F
b. 25 to 44 - E
c. 45 to 50 - D
d. 51 to 60 - C
e. 61 to 80 - B
f. Above 80 - A

Ask user to enter the marks and print the corresponding grade.
'''

marks=int(input("Enter the student marks: "))
if(marks<25):
    print("The student grade is F")
elif(marks>24 and marks<45):
    print("The student grade is E")
elif(marks>44 and marks<51):
    print("The student grade is D")
elif(marks>50 and marks<61):
    print("The student grade is C")
elif(marks>60 and marks<81):
    print("The student grade is B")
else:
    print("The student grade is A")
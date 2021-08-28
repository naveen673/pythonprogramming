#Description: This program prompts the user for their numeric grade
#and prints one of three messages depending on the grade.
'''
grade=int(input("Enter your grade: "))
if grade>=90:
    print("Very Good!")
elif grade>=60:
    print("Satisfactory.")
else:
    print("Poor")
'''

grade=int(input("Enter your grade: "))
if grade>=90:
    print("Very Good!")
elif grade>=80 and grade<=89:
    print("Good")
elif grade>=70 and grade<=79:
    print("Satisfactory")
elif grade>=60 and grade<=69:
    print("Fair")
else:
    print("Poor")
import math
#Program to calculate Student Grades
name=str(input('Enter student name:'))
eng=float(input('Enter English mark:'))
maths=float(input('Enter Maths mark:'))
social=float(input('Enter social mark:'))
science=float(input('Enter science mark:'))
pt=int(input('Enter PT mark:'))
total=eng+maths+social+science+pt
print('Total mark:',total)
grade=total//5
print('The grade point is:',grade)
if(grade>=80):
  print('Student work is Excellent')
elif(grade<80 and grade>60):
  print('Student work is Satisfied')
elif(grade<=60 and grade>40):
  print('Student work is good')
else:
    print('Student work needs improvement')

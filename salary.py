#calculate salary
import math
name=str(input('Enter employee name:'))
salary=float(input('Enter the basic salary:'))
def calculate_da(salary):
    if(salary<10000):
        da=(salary//100)*10
    elif(salary>=10000 and salary<25000):
        da=(salary//100)*12
    else:
        da=(salary//100)*14
    return da
def calculate_hra(salary):
    if(salary<10000):
        hra=(salary//100)*12
    elif(salary>=10000 and salary<25000):
        hra=(salary//100)*14
    else:
        hra=(salary//100)*17
    return hra
def total_salary(salary):
  total = salary+calculate_da(salary)+calculate_hra(salary)
  return total
print('The employee name is:', name)
print('The salary is:',salary)
print('Employee DA is',calculate_da(salary))
print('Employee HRA is',calculate_hra(salary))
print('The total salary is:',total_salary(salary))

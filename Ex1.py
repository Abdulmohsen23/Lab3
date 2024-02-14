
employees = {}
while(True):
   print('Please enter names of employees and their salaries until you finish: ')
   name = input('Name: ')
   salary = int(input('salary: '))
   employees[name] = salary
   flag= input('Do you want to continue? Yes or No !!').lower()
   if (flag == 'no'):
      break
   
print(employees)
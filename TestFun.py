#write a function that has two parameters Name and Age and call it with arguments.
def StudentInfo(name,age):
    print(f'My name is {name} and I am {age} Years Old.')
StudentInfo('Devid',23)
#Taking Aruments from user.
def StudentInfo1(Name,Age):
    print(f'My Name is {Name} and I am {Age} Years Old.')

name=input('Enter Your Name: ')
age=int(input('Enter Your Age: '))

StudentInfo1(name,age)








def student(grade,rollnumber):
    print(f'You are at {grade}th Grade and your rollnumber is {rollnumber}')

Grade=input('Enter Your Grade: ')
RollNumber=int(input('Enter Your RollNumber: '))
student(Grade,RollNumber)

def employee(ename,esalary):
    print(f'Your Name is {ename} and You have {esalary} salary')

Name='Rajesh'
Salary=4500
employee(Name,Salary)
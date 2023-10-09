class Student:
    def __init__(self,__name,__age):
        self.__name=__name
        self.__age=__age
    def StudentInfo(self):
        print(f'My Name is {self.__name} and I am {self.__age} Years Old.')
        return 'Thank You'

student1=Student('Sunna',22)
student2=Student('Harry',25)
print(student1.StudentInfo())
print(student2.StudentInfo())




"""The string representation of an object WITH the __str__() function:

"""
class Student:
    def __init__(self,name,roll_no,faculty,grade):
        self.Name= name
        self.Rol_No = roll_no
        self.Faculty =faculty
        self.Grade = grade

    def __str__(self):
        return f"{self.Name} {self.Rol_No} {self.Grade}  {self.Faculty}"

student_info = Student("John Doe", 102, "Computer Science", "3rdSemester")


print(student_info)
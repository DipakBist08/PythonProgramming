class StudentInfo:
    def __init__(self,name,RollNumber):
        self.name=name
        self.RollNumber=RollNumber
    def SInfo(self):
        print(f'Hello,I am {self.name} and My RollNumber is :{self.RollNumber}')


info=StudentInfo('Ramesh',14)
info1=StudentInfo('Herrry',15)
print(info.SInfo())
print(info1.SInfo())


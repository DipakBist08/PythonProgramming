class Student:
    def __init__(self,name,marks,age):
        self.name=name
        self.marks=marks
        self.age=age

    def AvgCalc(self):
        sum=0
        for val in self.marks:
            sum+=val
        print(f"Hi,{self.name},your average score is :",sum/3)


s1=Student("Harry",[97,77,89],19)
s1.AvgCalc()

s2=Student("Peter",[65,77,78],20)

s2.AvgCalc()

s2.name="Carry"
s2.AvgCalc()
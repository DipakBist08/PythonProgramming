class Students:
    def __init__(self,name,faculty,marks):
        self.name=name
        self.faculty=faculty
        self.marks=marks
        print("Adding students result to database.")


s1=Students("Sunil","BHM",77)
print(s1.name,s1.faculty,s1.marks)

s2 = Students("Dipak Bista","Bachelor Of Computer Application",98)
print(s2.name,s2.faculty,s2.marks)

s3 =Students("Ramesh","Arts", 79)
print(s3.name,s3.faculty,s3.marks)
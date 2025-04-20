class person:
    def __init__(self,name,age,contact_number):
        self.name=name
        self.age=age
        self.contactNumber=contact_number

person_info = person("Dipak Beesta",28,9825648134) #function call by creating an object
print(person_info) # this will print the memory location of person_info where it is located

print(person_info.name)
print(person_info.age)
print(person_info.contactNumber)
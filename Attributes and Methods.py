# Working with Attributes and Methods in Python
class PlayerCharacter:
    Membership = True  # This is class Attribute

    def __init__(self,name,age):
        if (self.Membership):
            self.name = name
            self.age = age
    def shout(self):
        print(f'My Name is {self.name} and my age is {self.age}')
Player1=PlayerCharacter('Cindy',33)
Player2=PlayerCharacter('Sunna',22)
print(Player1.shout())
print(Player2.shout())
print(Player1.Membership)

# Working with @classMethod and @staticmethod in Python
class PlayerCharacter:
    def __int__(self,name,age):
        self.name = name
        self.age = age

    def shout(self):
        return 'Hello'

    @classmethod
    def sum(cls,num1,num2):
        return num1 + num2
    @staticmethod
    def num_sum(x,y):
        return x+y

Player2=PlayerCharacter.sum(3,5)
Player3=PlayerCharacter.
print(Player2)


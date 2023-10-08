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
    def num_sum1(x,y):
        return x + y


print(PlayerCharacter.sum(2,5))
print(PlayerCharacter.num_sum1(6,8))

# here we haven't initiation  class without initiated we can call or printout the objects.

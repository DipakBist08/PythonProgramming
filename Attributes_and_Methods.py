class PlayerCharacter:
    membership=True
    def __init__(self,name,age):
        if(self.membership):
            self.name=name
            self.age=age
    def ShoutOut(self,Hello):
        print(f'My name is {self.name}')
        return 'Bye'

player1=PlayerCharacter('Cindy',22)
print(player1.name)
print(player1.age)
print(player1.membership)
print(player1.ShoutOut('Hi'))
class PlayerCharacter:
    def __init__(self,name,age):
        self.name = name
        self.age = age


    def run(self):

        print('Hello')
        return 'Done' #if here is not return keyword it will return none as default.


player1 = PlayerCharacter('Cindy',22)
player2 = PlayerCharacter('Hari',28)
print(player1.name)
print(player2.age)
print(player2.name)
print(player2.age)
print(player1.run())

#to display memory.
# print(player1)
# print(player2)
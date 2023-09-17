class PlayerCharacter:
    def __init__(self,name,age):
        self.name=name #Attributes
        self.age=age
    def run(self):
        print('run')
        return 'Done'
player1=PlayerCharacter('Sunna',20) #Objects
player2=PlayerCharacter('Harry',26)
print(player1.name)
print(player1.age)
print(player2.name)
print(player2.age)
print(player2.run())
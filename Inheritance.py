class User:
    def Login(self):
        print('Logged In Successfully!!!')


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'Wizard is attacking with power of {self.power}')


class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f'Archer is attacking with arrows: arrows left: {self.num_arrows}')


wizard1 = Wizard('Marlin', 101)
archer1 = Archer('Robin', 500)


wizard1.Login()
wizard1.attack()
archer1.attack()

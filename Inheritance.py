class User:
    def Sign_In(self):
        print('Logged In Successfully..')


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def Attack(self):
        print(f'Wizard is attacking with power of {self.power}')


class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def Attack(self):
        print(f'The archer is attacking with arrows.Left arrows:{self.num_arrows}')


wiz = Wizard('Kerry', 500)
arc = Archer('Rosey', 600)
wiz.Sign_In()
wiz.Attack()
arc.Attack()
print(wiz.name)
print(wiz.power)
print(arc.name)
print(arc.num_arrows)




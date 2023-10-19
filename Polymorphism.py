class User:
    def Sign_In(self):
        print('You are LoggedIn Successfully..')


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'The wizard is attacking with power of {self.power}.')


class Archer(User):
    def __init__(self, name, arrows):
        self.name = name
        self.arrows = arrows

    def attack(self):
        print(f'The archer is attacking with arrows:{self.arrows}')


wiz1 = Wizard('Robin', 420)
arc1 = Archer('Kerry', 101)

# First way to call method using polymorphism
# def Player_Attack(char):
#     char.attack()
# Player_Attack(wiz1)
# Player_Attack(arc1)

# by using for loop to access methods
for char in [wiz1, arc1]:
    char.attack()

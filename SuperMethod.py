class User(object):
    def __init__(self,email):
        self.email=email

    def Sign_In(self):
        print('LoggedIn Successfully..')

class Wizard(User):
    def __init__(self, name, power, email):
        super().__init__(email)
        self.name=name
        self.power=power

    def attack(self):
        print(f'wizard is attacking with power..')


wizard1=Wizard('Merlin',100,'merlin@gmail.com')
print(wizard1.email)
wizard1.attack()

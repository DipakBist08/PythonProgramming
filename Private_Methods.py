class Person:
    __name="anonymours"

    def __hello(self,name):
        print("Hello Person")


    def Welcome(self):
        self.__hello(self.__name)


p1 =Person()
print(p1.Welcome())


"""Recursive Function"""
def show(n):
    if n ==0:
        return n
    print(n)
    show(n-1)

show(5)

"""---Taking an Input from the user--"""
def Recuressin_Fun(UserInput):
    try:
        if UserInput==0:
            return UserInput

        print(UserInput)
        Recuressin_Fun(UserInput-1)

    except ValueError:
        print("Invalid Input!!!")

try:
    UserInput = int(input("Enter a number: "))
    Recuressin_Fun(UserInput)


except ValueError:
    print("Invalid Input, Please enter valid input!!!!")
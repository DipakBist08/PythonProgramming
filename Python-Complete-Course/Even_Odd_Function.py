
"""Method 1: Basic Function with Argument"""
def Even_Odd(num):

    if num % 2 == 0:
        print("Even Number")
    else:
        print("Odd Number!!!")

UserInput = int(input("Enter a number to find even or odd: "))

Even_Odd(UserInput)

"""Method 2: Function with User Input Inside"""

def even_odd(num):

    if num % 2 ==0:
        return  "Even Number"
    else:
        return "Odd Number"
num = int(input("Enter a number to find even or odd: "))
print(even_odd(num))

"""Method 4: Using Recursion"""

def Even_Odd():
    num = int(input("Enter a number to find even or odd: "))
    if num%2 ==0:
        print("Even Number")
    else:
        print("Odd Number.")
    choice = input("Do you want to check another number? (yes/No): ").lower()
    if choice=="yes":
        Even_Odd()
Even_Odd()


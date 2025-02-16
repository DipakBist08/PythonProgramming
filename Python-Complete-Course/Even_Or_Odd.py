#Even or Odd – Write a program that checks if a number entered by the user is even or odd.

print("Check Number 'Even' or 'Odd'")

try:
    UserInput = int(input("Check a number: "))
    if UserInput%2 ==0:
        print(f"{UserInput} is Even Number.")
    else:
        print(f"{UserInput} is Odd Number.")
except ValueError:
    print("Please Input a Valid Number!!")






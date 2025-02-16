#Largest of Three Numbers –
# Take three numbers as input and find the largest among them.

print("Find Largest Three Numbers")


try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    num3 = float(input("Enter third number: "))

    if num1==num2==num3:
        print("All are equal values")

    elif num1>num2 and num1>num3:
        print(f"{num1} the greatest number")
    elif num2>num3 and num2>num1:
        print(f"{num2} is the greatest number.")
    else:
        print(f"{num3} is greatest number.")
except ValueError:
    print("Invalid Input....!!")
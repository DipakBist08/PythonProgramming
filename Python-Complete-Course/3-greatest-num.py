print("Check Three Greatest Number")

try:
    num1 = float(input("Enter First Number: "))
    num2 = float(input("Enter Second Number: "))
    num3 = float(input("Enter Third Number: "))

    if num1>num2 and num1>num3:
        print(f"The {num1} is the greatest number.")
    elif num2>num1 and num2>num3:
        print(f"The {num2} is the greatest number.")
    elif num1==num2==num3:
        print(f"All Number are equal numbers")
    else:
        print(f"The {num3} is the greatest number")

except ValueError:
    print("Please Input Valid Input!!!!!")


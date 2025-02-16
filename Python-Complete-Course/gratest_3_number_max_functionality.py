print("Find Largest Three Numbers")


try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    num3 = float(input("Enter third number: "))

    largest_num = max(num1,num2,num3)
    #to ensure largest  number
    # print(largest_num)
    if num1==num2==num3:
        print("All are equal numbers.")
    else:
        print(f"The largest number is :{largest_num}")

except ValueError:
    print("Invalid Input....!")
def greater_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Input Valid Number..")

num1 = greater_number("Enter First Number: ")
num2 = greater_number("Enter Second Number: ")

if num1>num2:
    print(f"{num1} is greater than {num2}.")
elif num2> num1:
    print(f"{num2} is greater than {num1}.")
else:
    print(f"{num1} and {num2} are equal n8umbers")






#Triangle Validity – Take three sides of a triangle as input and determine if a valid triangle can be formed (sum of any two sides must be greater than the third side).
print("Triangle Validity Checker")
try:
    a = float(input("Enter first side: "))
    b = float(input("Enter second side: "))
    c = float(input("Enter third side: "))
    if a>0 and b>0 and c>0:
        if (a+b>c) and (a+c>b) and (b+c>a):
            print("The given sides form a valid triangle")
        else:
            print("Given sides can not be formed valid triangle!!!")
    else:
        print("Side length must be positive number")
except ValueError:
    print("Check Your Input !!!")
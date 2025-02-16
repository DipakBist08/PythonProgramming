#Grading System
from tokenize import Double

print("Check Your Grade :) ")
try:
    UserInput = float(input("Input Obtained Marks: "))
    if UserInput <=0 or UserInput>100:
        print("Please Input Number 1 to 100.")

    elif UserInput>=90:
        print("You got A Grade.")
    elif UserInput>=80:
        print("B")
    elif UserInput>=60:
        print("C")
    elif UserInput>=45:
        print("D")
    elif UserInput<45:
        print("Failled")
    else:
        print("Invalid Input")

except ValueError:
    print("Please Check Your Input Again")

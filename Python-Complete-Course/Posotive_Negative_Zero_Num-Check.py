#Positive, Negative, or Zero – Ask the user for a number and determine if it is positive, negative, or zero.

print("Check Entered Number is Positive,Negative or Zero!!")

try:
    UserInput = int(input("Enter a Number:  "))
    if UserInput>0:
        print("Positive Number.")
    elif UserInput=="0":
        print("Zero")
    else:
        print("Negative Number")
except ValueError:
    print("Please Enter Valid Number!!!")
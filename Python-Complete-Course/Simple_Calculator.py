def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    if b==0:
        print("Can not divide by 0.")

    return a/b


print("Choose Operations:")

print("1 for Add")
print("2 For subtract")
print("3 For multiplication")
print("4 for division")


choice = int(input("Enter your choice: "))


num1 = float(input("Enter First Number: "))
num2 = float(input("Enter the second number: "))

if choice==1:
    print("Result:", add(num1,num2))
elif choice==2:
    print("Result:",subtract(num1,num2))

elif choice==3:
    print("Result:",multiply(num1,num2))
elif choice==4:
    print("Resu:",divide(num1,num2))

else:
    print("Invalid Input")




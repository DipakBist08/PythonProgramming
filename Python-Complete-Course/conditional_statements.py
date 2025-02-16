"""Are you eligible for apply
driving licence? """

print("Are you eligible for apply driving licence?")

try:
    age = int(input("Enter your age: "))
    if age>=18:
        print("You are eligible for driving licence.")
    else:
        print("You are under age ")
except ValueError:
    print("Invalid Input!!! please enter age in digit.")

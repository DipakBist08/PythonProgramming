"""Electricity Bill Calculator –
Take electricity units as input and calculate the bill using this rate:

1-100 units → ₹5/unit --- 100*5
101-200 units → ₹7/unit --- (100*5) (101*200)
201+ units → ₹10/unit """

print("Calculate your electricity monthly bill")

try:

    consumed_unit = float(input("Enter total units consumed: "))
    if consumed_unit< 0:
        print("You do not have any bill.")
    else:
        if consumed_unit<=100:
            total_bill = consumed_unit*5
            print(f"Your Bill Amount is:Rs{total_bill}")
        elif consumed_unit<=200:
            total_bill = (100*5)+((consumed_unit-100)*7)
            print(f"Your Bill Amount is :Rs{total_bill}")
        else:
            total_bill = (100*5)+(100*7)+((consumed_unit-200)*10)
            print(f"Your Bill Amount is:Rs {total_bill}")
except ValueError:
    print("Please enter valid input!!!")

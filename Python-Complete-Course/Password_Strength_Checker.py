# Password Strength Checker –
# Take a password as input and check if it is strong
# (must contain at least one uppercase letter, one lowercase letter, one digit, and one special character).
import re
print("Check Your Password Strength:)")
password = input("Enter Your Password Here: ")
has_upper =re.search(r"[A-Z]",password)
has_lower = re.search(r"[a-z]",password)
has_digit = re.search(r"[0-9]",password)
has_special = re.search(r"[!@#$%^&*(),.?\":{}|<>]",password)
is_long_enough = len(password)>=8
if has_upper and has_lower and has_special and has_digit and is_long_enough:
    print(f"Your password is strong:)")
elif len(password)<8:
    print("Your password must be 8 characters long")
else:
    print("Medium password!!")


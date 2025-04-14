users = {
    "dipak":"P@ssw0rd@121#",
    "sunil":"sunil@121#",
    "Ramesh":"Pass@123",
    "Vijaya":"Secret11@"

}

userName = input("Enter User Name: ")
userPass = input("Enter User Password: ")
if userName in users:
    if users[userName]==userPass:
        print("Login Successful")
    else:
        print("Invalid credentials!!!")
else:
    print("User Not Found!!!!")

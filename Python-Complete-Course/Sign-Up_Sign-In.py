# from Login_System_Using_Dict import users


users = {
    "dipak":"P@ssw0rd@121#",
    "sunil":"sunil@121#",
    "Ramesh":"Pass@123",
    "Vijaya":"Secret11@"

}

choice = input("Sign-In/Sign-Up: ")
if choice=="Sign-Up":
    new_userName = input("Enter a User Name: ")
    if new_userName in users:
        print("User already exists!!")
    else:
        new_pass = input("Enter your Password: ")
        users[new_userName]=new_pass
        print("Sign-Up Successfully.")

elif choice =="Sign-In":
    userName = input("Enter User Name: ")
    userPass = input("Enter Password: ")
    if userName in users and users[userName] ==userPass:
        print("Sing-In Successful")
    else:
        print("Invalid Credentials!!!!")




class BankDetails:
    def __init__(self,acc_no,acc_pass):
        self.__acc_no=acc_no #By __ we can make the objects private and will not be accessed outside the class
        self.__acc_pass=acc_pass
        # print(self.__acc_pass)

    def resetPassword(self):
        print(self.__acc_pass)
        print(self.__acc_no)




Account_1=BankDetails(1232,"P@ssword@121")

print(Account_1.resetPassword())

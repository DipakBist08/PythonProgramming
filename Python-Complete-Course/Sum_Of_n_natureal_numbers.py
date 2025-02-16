# #take an input from user and calculate sum of that entered number.
# try:
#     Sum_Num = int(input("Enter a number you want to get sum of it: "))
#
#     sum = 0
#     for calc in range(1,Sum_Num+1):
#         sum+=calc
#     print(f"The total sum of {Sum_Num} is: {sum}")
#
# except ValueError:
#     print("Please Valid Input!!")



User_Input = int(input("Enter a number  to get sum: "))
sum = 0
for i in range(0,User_Input+1):
    sum+=i
    print(sum) # If you print form this state  you will see executing each iteration result
print(sum) #If you print this indent then you will see result of final execution overall sum of a number.




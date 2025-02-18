"""Write a program calculate of a number using while loop."""


User_Input = int(input("Enter a number to get sum of it: "))

sum = 0
i = 1
while i <=User_Input:
    sum+=i
    i+=1
print(sum)
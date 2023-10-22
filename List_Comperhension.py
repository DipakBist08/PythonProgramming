My_List=[]
for char in 'Hello Programmers':
    My_List.append(char)
    print(My_List)
print('This is Outer Print Function...')
print(My_List)

print('Short and Cleaner way to write it')
My_List1=[char for char in 'Hello Programmers']
print(My_List1)
My_List2=[num for num in range(0,100)]
print(My_List2)
My_List3=[num*num for num in range(1,5)]
print(My_List3)
My_List4=[num**2 for num in range(1,5)]
print(My_List4)

#To print Only Even Number form number 0 to 100
Even_List=[num for num in range(0,100) if num%2==0]
print(Even_List)
#To print Odd Numbers only
Odd_List=[nums for nums in range(0,100) if nums%2 !=0]
print(Odd_List)


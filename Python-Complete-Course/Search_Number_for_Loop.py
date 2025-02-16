myList = [1,2,3,4,5,6,7,8,11,12,13,14,15,16,17,18,19,21,100,101,19]
x = 19
for element in myList:
    if element ==x:
        print("Found at index",element)
    else:
        print("Searching....")
        element+=1

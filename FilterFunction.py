def Odd_Only(item):
    return item % 2 != 0


My_List = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(filter(Odd_Only, My_List)))


def Even_Only(item):
    return item % 2 == 0


List_Filter = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 13, 13, 15]

print(list(filter(Even_Only,List_Filter)))
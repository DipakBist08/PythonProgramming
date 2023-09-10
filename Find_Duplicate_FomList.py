# #Exercise :Find the Duplicate values from the list and store those duplicate values in duplicates list
# duplicate_List=['a','b','a','c','d','c','e','b','e','f']
#
# duplicates=[]
# for value in duplicate_List:
#     if duplicate_List.count(value)>1:
#         if value not in duplicates:
#             duplicates.append(value)
# print(duplicates)



#findout specific duplicate value how many times repeated.
duplicate_List = ['a', 'b', 'a', 'c', 'd', 'c', 'e', 'b', 'e', 'f']
count_dict = {}

for value in duplicate_List:
    if value in count_dict:
        count_dict[value] += 1
    else:
        count_dict[value] = 1

for key, value in count_dict.items():
    print(f'The value "{key}" appears as a duplicate {value} times.')

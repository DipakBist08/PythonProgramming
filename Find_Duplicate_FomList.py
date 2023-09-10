#Exercise :Find the Duplicate values from the list and store those duplicate values in duplicates list
duplicate_List=['a','b','a','c','d','c','e','b','e','f']

duplicates=[]
for value in duplicate_List:
    if duplicate_List.count(value)>1:
        if value not in duplicates:
            duplicates.append(value)
print(duplicates)
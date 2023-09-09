#This is also another important datastructure in python.
#It only returns the unique data type.It dosen't support the duplicate elements.

my_set={
    100,101,101,102,103,104,105
}
my_set.add(106) #add() add only one argument.
print(my_set) #output: {100, 101, 102, 103, 104, 105, 106}
print(len(my_set)) #will display how many unique elements are present in that set.It will not  count the duplicate elements.

#It will count form one not form zero.


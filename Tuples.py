#Tuples are like List but we can't modify them like List we.Tuples are Immutable.

my_tuple=(1,1,3,3,5,2,3,4)
print(my_tuple)

# my_tuple[1]='0' #TypeError: 'tuple' object does not support item assignment
print(my_tuple[1])

print(5 in my_tuple) #True

#The best use of tuple is when user need a everytime new request.Example :Pathawo and Indrive.

#here how can you define the tuple
x,y,z,*other=(1,2,3,4,5)
print(x) #x=1
print(y) #y=2
print(z) #z=3
print(other) #[4, 5, 6, 7, 8]
print(my_tuple.count(3)) #will count how many 3 are present in my_tuple
print(my_tuple.count(7)) #will count how many seven are present in my_tuple

print(my_tuple.index(5)) #will display the index of that element in the tuple

print(len(my_tuple)) # will count the length of that tuple
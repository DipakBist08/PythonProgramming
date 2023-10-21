def square(n):
    return n*2
MyList=[1,2,3,4,5]
for item in MyList:
    print(list(map(square,MyList)))

def cube(n):
    return n*3
My_List=[2,3,4]
print(list(map(cube,My_List)))

def myMapFunc(n):
    return n.upper()

StringList=['apple','windows','unix','linux']
print(list(map(myMapFunc,StringList)))
print(map(myMapFunc,StringList))  #will print memory location of map object.


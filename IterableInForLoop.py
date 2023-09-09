#iterable is an object ot set of collection that can be interative over and over again.
#Means one by one check each item in the collection
#iteral can be : List,Tuple,Set  or String

#Basically there are Three Methods
#keys(),values() and items()
User={
    'name':'Dipak Bista',
    'age': 28,
    'is_Handsome':True,
    'Programming_Expert':False
}

for info in  User:
    print(info) #will print the keys of the dictionary

#will display the keys and values all the items inside the dictionary
for info in User.items():
    print(info)

#will display keys User Dictionary
for info in User.keys():
    print(info)

#Will printout the values of User Dictionary

for info in User.values():
    print(info)

# or another way to define the variables in for loop

for key,value in User.items():
    print(key,value)
    #Note the key and value variable can be anything like x,y

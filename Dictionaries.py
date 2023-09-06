#Dictionary is an unordered key value pair.In Python we call it datastructure as well.
#Syntax: 'a':4 . Here 'a' is a string key and 5 is a value.
# Dictionary={
#     'a':5,
#     'b':7
# }
# #will print 'b' value 7
# print(Dictionary['b']) #output: 7

cart={
    'basket':[1,2,3,4],
    'available_Items':203,

    'brand':"XYZ",
    'is_Durable':True
}
#print all the content inside the dictionary
print(cart)
#only print the value of 'basket'
print(cart.get('basket'))
#will display bool value
print('basket' in cart)

#will display all the items inside the cart dictionary
print(cart.items())
#will display values only
print(cart.values())
#will display keys only
print(cart.keys())

#To make a copy of  the dictionary
print(cart.copy())
#will remove brand from the dictionary
print(cart.pop('brand'))
print(cart)

#update the dictionary
print(cart.update({'available_Items':333}))
print(cart)

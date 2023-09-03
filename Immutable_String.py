#Strings are Immutable until you will destroyed you that string you can't change it's assigned value.
#Here is a example of Immutable String :
quote='to be or not to be'
quote2=quote.replace('be','me') #here we have defined seperate variable to replace the string we can't change same string
print(quote2)
#Immutable qupte
print(quote)
print(len(quote2))
print(len(quote2[0:]))

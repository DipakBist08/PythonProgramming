#Strings are Immutable
#here are some string methods
quote='to be or not to be'
print(quote.title()) #will make the quote like Title.
print(quote.upper()) #will make the quote's string in Upper case letter
print(quote.upper()) #Will display  string letter in lower case
print(quote.find('or')) #will display the index of the or string
print(quote.replace('be' ,'you')) #will replace 'be' by 'you'
print(quote) #here string value remains same because string is immutable we can't change their value.

quote2=quote.replace('be','me')
print(quote2) #output: to me or not to me
print(quote) #output: to be or not to be

#Untill you destroyed or Declared new string, you can't change the value once it has declered.


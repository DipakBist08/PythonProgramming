strn1 = "This is a string.\n Now You can write this line in a new  line...\n"
print(strn1)

#String Concatenation

str2 = "Welcome to the concatenation"


final_string = strn1+str2

print(final_string)
#len function will display total length of the strings
print(len(final_string))


#Index of strings

print(final_string[12])

#str1 string length
print(len(strn1))


# String Slicing it will start from 0 and  less than specified number

print(strn1[1:4])

#To go till last letter of string
print(strn1[22:len(strn1)])


#Reverse or Negative Indexing

print(str2[-22:-1])

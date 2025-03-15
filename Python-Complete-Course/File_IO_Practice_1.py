with open("test.txt","a+") as f:
    f.write("Hi Everyone, I am working with file handling.\n Let's learn together.... ")
    f.close()

with open("test.txt","r") as f1:
    data = f1.read()

print(data)
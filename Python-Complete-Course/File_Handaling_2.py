f = open("test.txt","w")
f.write("This line will override entire content of the file.")

f.close()
f1 = open("test.txt")
content_show = f1.read()
print(content_show)
f1.close()
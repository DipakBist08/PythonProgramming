f = open("test.txt")
""".radline() is used to read data line by line from the file"""
data = f.readline()
f.close()
print(data)


file = open("test.txt")
""".read() is used to read entire file at once.."""
data = file.read()
print(data)

f.close() 
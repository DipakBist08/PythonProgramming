"Create a new file named 'practice.txt' using python. Add the following data in it."

"""
Hi everyone
I am learning File I/O
using Python.
I like programming in Python.
"""


with open("practice.txt","w") as f:
    f.write("Hi everyone \n I am learning File I/O \n using python.\n I like programming in python.")
    f.close()

with open("practice.txt","r") as f:
     data = f.read()
     print(data)
     f.close()
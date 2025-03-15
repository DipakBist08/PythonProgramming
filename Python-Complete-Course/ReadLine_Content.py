file_path = "sample.txt"
with open(file_path,"r") as file:
    read_content = file.readline(50) # this will read upto 50 characters from the file for specific line means first line
    read_contents = file.readlines() #it will read content line by line.


print(read_content)

print(read_contents)
file.close()

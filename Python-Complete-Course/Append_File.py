file_path = "sample.txt"
with open(file_path,"a") as file:
    file.write("This is appended file to the 'sample.txt' file")

    file.close()
with open(file_path,'r') as file:
    read_content = file.read()

print(read_content)
file.close()

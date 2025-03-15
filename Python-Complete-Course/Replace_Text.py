file_path ="ReplaceText.txt"
with open(file_path,"r") as file:
    data= file.read()
new_data = data.replace("Java","Python")
print(new_data)

#To override on this file

with open(file_path,"w") as f:
    override_data = f.write(new_data)
print(override_data)
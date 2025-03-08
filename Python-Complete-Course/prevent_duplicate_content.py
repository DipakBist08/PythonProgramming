file_path ="content.txt"
new_content = input("Enter Content: ")
with open(file_path,"r") as f:
    exiting_content = f.read()
if new_content not in exiting_content:
    with open(file_path,"a") as f:
        f.write("\n" + new_content)

    print("New Content added successfully.")
else:
    print("This content is already exists in the file!!!!")
f.close()

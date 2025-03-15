file_path = "ReplaceText.txt"
word ="learning"
with open(file_path,"r") as f:
    read_data =f.read()
    if read_data.find(word) !=-1:

        print("Found")
    else:
        print("Not Found")
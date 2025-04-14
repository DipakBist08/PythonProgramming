files=[
    ("report.pdf","2MB","2025-04-14"),
    ("data.csv","1MB","2025-04-13")
]

for fileName,fileSize,data in files:
    print(f"{fileName} was created on {data} and is {fileSize} in size")

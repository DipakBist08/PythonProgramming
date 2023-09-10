# Function is very powerful concept in python.It is basically DRY(Don't Repeat Yourself).

def Show_Tree():
    picture = [
        [0,0,0,1,0,0,0],
        [0,0,1,1,1,0,0],
        [0,1,1,1,1,1,0],
        [1,1,1,1,1,1,1],
        [0,0,0,1,0,0,0],
        [0,0,0,1,0,0,0]

    ]
    for row in picture:
        for pixel in row:
            if pixel == 1:
                print('*',end='')
            else:
                print('',end='')
        print('')

Show_Tree() #Function called
Show_Tree() #Function called Again
Show_Tree() #Function called Again and Again
Show_Tree() #Function called  Again,Again and Again means you can call the function so many times without writing same code multiple times.

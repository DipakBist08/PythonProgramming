# it will print from 0 to 10.
i = 0
while i <= 10:
    print(i)
    i += 1

# Will run infinite loop untill the system crash.
# i =0
# while i<1:
#     print(i)

# #if the user don't know how many time will be looping
# while True:
#     input('Say Something: ')

# untill run the program response == bye

while True:
    response = input('Say Something:')
    if response == 'bye':
        print(response)
        break
    else:
        print('Well Done')
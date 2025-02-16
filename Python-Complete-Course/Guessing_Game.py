import  random
random_num = random.randint(1,10)
user_guess = None
while user_guess!=random_num:
    user_guess = int(input("Guess a number between 1 to 10: "))
    if user_guess==random_num:
        print("Congrats! You guessed it right.")
    else:
        print("Try Again!!!")
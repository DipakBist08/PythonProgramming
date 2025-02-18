def find_factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact*=i
    print(fact)

find_factorial(5)
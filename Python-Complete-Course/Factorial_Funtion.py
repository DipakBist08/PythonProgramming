def factorial_fun(n):
    if n ==0 or n ==1:
        return 1
    return factorial_fun(n-1)*n
print(factorial_fun(5)) 
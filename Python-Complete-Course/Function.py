#Function Definition
def Calc_Sum(a,b): # parameters
    return a+b
sum = Calc_Sum(19,20) #Arguments or values
print(sum)

#Calculation for Subtraction of two digits.
def Calc_Sub(a,b):
    return a-b
sub = Calc_Sub(78,21)
print(sub)

#Function with default parameters
def Default_Params(a,b=9):
    return a*b
obj = Default_Params(6)
print(obj)

#Function with division
def Calc_Div(a,b):
    return a/b
div = Calc_Div(18,9)
print(div)

#Calculate Average of three numbers using a funciton
def Calc_Avg(a,b,c):
    sum = a+b+c
    avg = sum/3
    return avg
avg_obj = Calc_Avg(1,2,9)
print(avg_obj)


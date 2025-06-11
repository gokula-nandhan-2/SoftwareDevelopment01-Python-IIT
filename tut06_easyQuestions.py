#question 1
def addNumbers(a,b,c):
    sum = a+b+c
    return sum

#question 2
def multiply(a,b):
    mul = a*b
    return mul

#question 3
def average(a,b,c):
    tot = a+b+c
    ave = tot /3
    return ave

#question 4
def maximum(a,b):
    max=0
    if a>b:
        max = a
    else:
        max = b
    return max 

#question 5
def perimeters(len,wid):
    peri = (len + wid)*2
    return peri
#rectangle has 2 length(lengths are same) and 2 width(widths are same)

#question 6
def convertion(fahrenheit):
    celcius = (fahrenheit - 32) * 5/9
    return celcius

#question 7
def primeNumber(num):
    if num==1:
        return False
    
    for i in range(2,num):
        if num % 2==0:
            return False
        else:
            return True




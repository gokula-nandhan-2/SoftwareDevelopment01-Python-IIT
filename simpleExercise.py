# task01
num = int(input("Enter a number: "))
if num % 5 == 0:
    print("Divisible by 5")

# task02
age = int(input("Enter your age: "))
if age < 18:
    print("You are not eliglible to vote")
else:
    print("You are eligible to vote")

# task03
num1 = int(input("Enter first number: "))

if num1 > 0:
    print("Positive")
elif num1 < 0:
    print("Negative")
else:
    print("Zero") 


# task04
num2 = int(input("Enter a number: "))
if 0 < num2 <= 10:
    if num2 % 2 == 0:
        print("Even")
    else:
        print("Odd")      
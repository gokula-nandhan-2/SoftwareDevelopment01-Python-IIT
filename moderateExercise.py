# task05
year = int(input("Enter a year: "))
if year % 4 ==0:
    print("Leap year")

# task06
print("\n")
letter = input("Enter a letter: ")
vowels = "aeiou"
if letter in vowels:
    print("The letter is a vowel")
else:
    print("The letter is a consonant")   

# task07
print("\n")
char = input("Enter a character: ")

if char.isupper():
    print("The character is uppercase")
elif char.islower():
    print("The character is lowercase")
elif char.isdigit():
    print("The character is a digit")
else:
    print("The character is a special character")

# task08
print("\n")
amount = float(input("Enter the amount: "))
discount = 0

if amount > 1000:
 discount = amount * (10/100)
elif amount <= 1000 or amount > 500:
 discount = amount * (5/100)
else:
 discount = 0

print(f"The discount is: {discount}")
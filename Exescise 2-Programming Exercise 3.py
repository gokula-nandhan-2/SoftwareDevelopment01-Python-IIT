# String Analyzing Program

phrase = input("Type something : ")

if phrase.isupper():
    print("The phrase is in uppercase.")

if phrase.islower():
    print("The phrase is in lowercase.")

if phrase.isalpha():
    print("The phrase contains only alphabetic characters.")

if phrase.isdigit():
    print("The phrase contains only digits.")

if phrase.isspace():
    print("The phrase contains only whitespace characters.")

if phrase.startswith("s"):
    print("The phrase starts with the letter 's'.")

if phrase.endswith("t"):
    print("The phrase ends with the letter 't'.")

if phrase.count("e") >= 2:
    print("The phrase contains the letter 'e' at least twice.")

print("The length of the phrase is:", len(phrase))

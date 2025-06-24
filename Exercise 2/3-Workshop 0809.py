# Exercise 2 - Workshop 0809
def checkPassword1(pword):
    shortEnough = False
    longEnough = False
    hasUpper = False
    hasLower = False
    hasSpecial = False
    specialChars = '\'~!#$%^*()_+-={}|[]\\:<>?,./'

    if len(pword) <= 16:
        shortEnough = True
    if len(pword) >= 8:
        longEnough = True
    
    for char in pword:
        if char.isupper():
            hasUpper = True
        if char.islower():
            hasLower = True
        if char in specialChars:
            hasSpecial = True
    
    if shortEnough and longEnough and hasUpper and hasLower and hasSpecial:
        return True
    else:
        return False
    
# Exercise 3 - Workshop 0809
def checkPassword2(pword):
    hasUpper = False
    hasLower = False
    hasSpecial = False
    specialChars = '\'~!#$%^*()_+-={}|[]\\:<>?,./'

    if len(pword) > 16 or len(pword) < 8:
        return False
    
    for char in pword:
        if not hasUpper and char.isupper():
            hasUpper = True
        elif not hasLower and char.islower():
            hasLower = True
        elif not hasSpecial and char in specialChars:
            hasSpecial = True
            
        if hasUpper and hasLower and hasSpecial:
            return True

    return False

password = input('Enter your password: ')
if checkPassword2(password):
    print('Your password is valid.')
else:
    print('Your password is not valid.')
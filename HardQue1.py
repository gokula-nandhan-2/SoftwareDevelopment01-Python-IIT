def calculator(num1,num2,operator):
    
    if operator == "+":
        add = num1 + num2
        return add
    elif operator == "-":
        sub = num1 - num2
        return sub
    elif operator == "*":
        mul = num1 * num2
        return mul
    else:
        if num2 == 0:
            print("Cannot divide by zero")
        else:
            div = num1 / num2
            return div


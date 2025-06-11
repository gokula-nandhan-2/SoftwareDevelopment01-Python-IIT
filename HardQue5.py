def exponentiation(base,exponent):
    if exponent == 0:
        return 1      
    else:
        answer = base * exponentiation(base,exponent-1)    
        return answer
    

print(exponentiation(2,3))
def even_or_odd(num):
    div=2
    if num & (div>>1):
        return "Odd Number"
    else:
        return "Even Number"

print(even_or_odd(2))
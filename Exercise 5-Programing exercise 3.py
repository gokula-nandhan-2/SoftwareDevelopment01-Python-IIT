# Income Tax Program

income = float(input("Enter your income: "))

if income > 0 and income <= 18200:
    tax = 0
elif income > 18200 and income <= 37000:
    tax = (income - 18200) * 0.19
elif income > 37000 and income <= 80000:
    tax = 3572 + (income - 37000) * 0.325
elif income > 80000 and income <= 180000:
    tax = 17547 + (income - 80000) * 0.37
else:
    tax = 54547 + (income - 180000) * 0.45

print(f"Your income tax is: ${tax:.2f}")
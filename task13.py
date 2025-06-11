height = float(input("Enter the height in meters: "))
weight = float(input("Enter the weight in kilograms: "))

bmi = weight / (height ** 2)
print(f"Your BMI is: {bmi:.2f}")
# Enhancing a Conversion Program

print("""Print Options
      1 for Matric to Imperial
      2 for Imperial to Metric      """)


option = input("Choose an option (1 or 2): ")

if option == '1':
    meters = float(input("Enter distance in meters: "))
    feet = meters * 3.28084
    print(f"{meters} meters is {feet:.2f} feet.")
elif option == '2':
    feet = float(input("Enter distance in feet: "))
    meters = feet / 3.28084
    print(f"{feet} feet is {meters:.2f} meters.")
else:
    print("Invalid option selected. Please choose 1 or 2.")
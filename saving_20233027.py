target=int(input("Enter your target savings goal amount :"))
current=int(input("Enter your current savings amount :"))
monthly=int(input("How much you can save monthly? :"))

balance=target-current
terms=balance/monthly
round(terms)

print("You target savings goal amount is Rs.",target)
print("You current savings amount is Rs.",current)
print("you have to save Rs.",balance,"to achieve your goal")
print("You are saying you can save monthly Rs.",monthly)
print("So,you wan't to save money for",terms,"months")
print("Good luck!")


#i cannot get value without decimal points for month

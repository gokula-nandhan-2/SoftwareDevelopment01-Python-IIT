# Exercise 4

marks = []
rate = []

for i in range(1,6):
    s=int(input(f"Enter your marks for subject {i} :"))
    s_rate = input("Did you pass the exam?(y/n): ")
    marks.append(s)
    rate.append(s_rate)

total = sum(marks)
average=total/5

failed = False
for i in range(0,5):
    if marks[i] >= 50 and rate[i].lower() == 'n':
        failed = True
        break

if failed:
    print("Grade: Fail/Incomplete")
else:
    if average >= 90:
        grade = "A+"
    elif average >= 80:
        grade = "A"
    elif average >= 70:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 50:
        grade = "D"
    else:
        grade = "F"
    print("Grade:", grade)

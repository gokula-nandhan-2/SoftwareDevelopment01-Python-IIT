s1=int(input("Enter your marks for subject 1 :"))
s2=int(input("Enter your marks for subject 2 :"))
s3=int(input("Enter your marks for subject 3 :"))
s4=int(input("Enter your marks for subject 4 :"))
s5=int(input("Enter your marks for subject 5 :"))


total=s1+s2+s3+s4+s5
average=total/5

print(average)

if average>=50:
    print("Good average")
else:
    print("Bad average")

#Coursework counts for 40% of the final grade.
#Midterm exam counts for 25%.
#Final exam counts for 35%.


cw=int(input("Enter your coursework marks :"))
#cw means course work
if 0<=cw<=100:
    print("your coursework mark is",cw)
else:
    print("Invalid marks")
    

me=int(input("Enter your midterm exam marks :"))
#me means midterm exam marks
if 0<=me<=100:
    print("your coursework mark is",me)
else:
    print("Invalid marks")
    

fe=int(input("Enter your final exam marks :"))
#e means final exam marks
if 0<=fe<=100:
    print("your coursework mark is",fe)
else:
    print("Invalid marks")
    


tot=(40/100*cw)+(25/100*me)+(35/100*fe)
print("Your numoric final grade is",tot)

if 0<=tot<=100:
    if 70<=tot<=100:
        print("Your letter grade is A")
    elif 50<=tot<=69:
        print("Your letter grade is B")
    elif 40<=tot<=49:
        print("Your letter grade is c")
    else:
        print("Your letter grade is F")
else:
    print("Invalid marks")


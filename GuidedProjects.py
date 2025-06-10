#guided projects
#all the shell are done in the terminal

# 1.Quadratic Equation Solver
a = int(input("Enter coefficient a: "))
b = int(input("Enter coefficient b: "))  
c = int(input("Enter coefficient c: "))

quradric = - b + (b^2 - 4*a*c)**0.5 / (2*a)
print("The solution 1 is:", quradric)

quradric = -b - (b^2 - 4*a*c)**0.5 / (2*a)
print("The solution 2 is:", quradric,"\n")


# 2.Area of a Circle 
radius = float(input("Enter the radius of the circle: "))
area = 3.14 * radius**2
print("The area of the circle is:", area,"\n")


# 3.Salary Increase Calculator
current_salary = float(input("Enter your current salary: "))
increase_percentage = float(input("Enter the percentage increase: "))

new_salary = current_salary + (current_salary * increase_percentage / 100)
print("Your new salary after the increase is:", new_salary, "\n")


# 4.volume of a Cylinder
radius = float(input("Enter the radius of the cylinder: "))
height = float(input("Enter the height of the cylinder: "))

volume = 3.14 * radius**2 * height
print("The volume of the cylinder is:", volume, "\n")

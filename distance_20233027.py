x1=int(input("Enter the x value for the first coordinate(x1) :"))
y1=int(input("Enter the y value for the first coordinate(y1) :"))

print("your first coordinate point is (",x1,",",y1,")")

x2=int(input("Enter the  x value for the second coordinate(x2) :"))
y2=int(input("Enter the  y value for the first coordinate(y2) :"))


print("your second coordinate point is (",x2,",",y2,")")
print("it is time to calculate distance of the two coordinates")

x=x2-x1
y=y2-y1

sq_of_distance=(x**2)+(y**2)

distance=math.sqrt(sq_of_distance)
#i cannot write a function get square root for "sq_of_distance"
#programme crashed

print("The distance between two coordinates is",distance)


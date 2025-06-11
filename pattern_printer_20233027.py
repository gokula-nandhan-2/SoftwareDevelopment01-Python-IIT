levelno=int(input("Enter number of levels :"))
for n in range(1,levelno+1):
    for space in range(levelno,n,-1):
        print(" ",end="")
    for star in range(1,n*2):
        print("*",end="")

    print()
        
        
    

n = int(input("Enter a starting number :"))

while n!=1:
    print(int(n))
    if n%2==0:
        n=n/2
    else:
        n=3*n+1


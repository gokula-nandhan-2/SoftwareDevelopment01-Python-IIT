for i in range(3,1001):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        k=i+2
        for m in range(2,k):
            if k%m==0:
                break
        else:
            print(i,k,"-Twin prime numbers")
        

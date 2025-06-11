for i in range(2,1001):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        si=str(i)
        if si[0]==si[len(si)-1]:
            print(i)

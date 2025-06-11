count=0
for i in range(101,200):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i)
        count+=1
        if count==10:
            break

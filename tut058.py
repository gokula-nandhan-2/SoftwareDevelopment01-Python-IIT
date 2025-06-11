list=["A","B","C"]

for i in range(len(list)):
    for j in range(len(list)):
        for k in range(len(list)):
            if i!=j and j!=k and i!=k:
                print(list[i]+list[j]+list[k])
 
        

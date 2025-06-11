list1=[[1,2,3],[4,5,6],[7,8,9]]
list2=[]

def flatten():
    for i in range(0,len(list1)):
        for j in range(0,3):
            list2.append(list1[i][j])

    tot=0
    for k in range(0,len(list2)):
        tot+=list2[k]

    return tot
    
print(flatten())
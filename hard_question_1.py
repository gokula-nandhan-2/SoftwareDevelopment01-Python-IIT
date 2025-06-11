list=[[2,3],[4,5,6],[],[6],[7,8,9]]

def maximum():
    max=[]
    for i in range(0,len(list)):
        if len(max)<len(list[i]):
            max=list[i]
            
    return max

print(maximum())
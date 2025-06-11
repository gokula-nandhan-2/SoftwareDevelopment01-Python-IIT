list1=[[1,2],[3],[4,5]]
list2=[]

def sum_of_the_list1():
    sum=0
    for i in range(0,len(list1)):
        for j in range(0,len(list1[i])):
            list2.append(list1[i][j])
        
            
    for k in range(0,len(list2)):
        sum+=list2[k]
    return sum
        
    
            

print(sum_of_the_list1())
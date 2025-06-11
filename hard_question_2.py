list=[(1,2),(3,4)]
newList=[]
sum=0

for i in range(0,len(list)):
    for j in range(0,len(list[i])):
        sum+=list[i][j]
    newList.append(sum)
    sum-=sum
print(newList)
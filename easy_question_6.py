list1=[1,2,3,4,5,6,7,8,9,10]

list2=[list1[i]*2 for i in range(0,len(list1)) if list1[i]%2==1]

print(list2)
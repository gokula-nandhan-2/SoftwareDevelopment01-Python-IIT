list1=[1,-1,2,-2,3,-3,4,-4,5,-5,6]

def positive_number_list():
    list2=[list1[i] for i in range(0,len(list1)) if list1[i]>0]
    return list2

print(positive_number_list())
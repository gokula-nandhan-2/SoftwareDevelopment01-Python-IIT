list=[1,2,3,4]

def product_of_a_list():
    product=1
    if list == []:
        return 1
    else:
        for i in range(0,len(list)):
            product *= list[i]
        return product

print(product_of_a_list())
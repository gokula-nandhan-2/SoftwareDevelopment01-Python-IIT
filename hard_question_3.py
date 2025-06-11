tuple=("Machine"," ","Learning"," ","Engineer")


def concatination():
    string=""
    for i in range(0,len(tuple)):
        string+=tuple[i]
    return string

print(concatination())
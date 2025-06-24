import json


students = {60254: 'John Smith', 
            60255: 'Gert Hans-Dyer', 
            60256: 'Sun Po', 
            60257: 'Bort Woods', 
            60258: 'Andrew Butters', 
            60259: 'Betty Ho',
            60260: 'Jonah Smithers', 
            60261: 'Sha Po', 
            60262: 'Jane Smitt'}
usernames = {}

# Exercise 5
def resolveDuplicate(username, usernames):
    counter = 0
    while True:
        counter += 1
        new_username = username + str(counter)
        if new_username not in usernames.values():
            return new_username
        

for i in students.items():
    split_name = i[1].lower().replace("-","").split()
    username = split_name[0][0] + split_name[1][0:4]
    if len(username) < 4:
        username = username.ljust(4,"0")
    if username in usernames.values():
        username = resolveDuplicate(username, usernames)
    usernames[i[0]] = username
    print(f"{i[0]}: {username}")

print(usernames)

with open("usernames.json", "w") as file:
    json.dump(usernames, file, indent=4)



    

        
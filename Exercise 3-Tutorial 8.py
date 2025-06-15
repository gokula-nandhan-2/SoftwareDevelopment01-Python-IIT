# Exercise 3

# --- getList(filename), returns a list of strings --- 
# (open/create file and return lines of text as a list of strings) 


filename = 'C:\Users\Gokul\Projects\softwareDevelopment01-Python-IIT\todo.txt'
# Define the filename used to store the list
  
# Define the filename used to store the list
def getList(filename): 
    data = []
    try:
        file = open(filename, "r")
        data = file.readlines()
        file.close()
    except FileNotFoundError:
        file = open(filename,"w+")
        data = []
        file.close()
    return data


# --- showList(data), returns nothing --- 
# (receive list of strings and display them, or "nothing in list" message) 
def showList(data):
    if len(data) == 0:
        print("Your To Do List is empty.")
    else:
        print("To Do List:")
        for i in range(len(data)):
            print(f"{i}) {data[i]}")  


# --- addToList(filename, data), returns a list of strings --- 
# (prompt for an item to add to the list of strings and append to the file) 
def addToList(filename, data): 
    return data 


# --- deleteFromList(filename, data), returns a list of strings --- 
# (prompt for item number to delete from the list of strings and write list to the file) 
def deleteFromList(filename, data): 
    return data 

# --- main part of program --- 
FILENAME = 'list.txt' # define the filename used to store the list 
lineList = getList(FILENAME) # call the getList function to read the file into a list
#print(lineList)  

while True: # this endless loop displays the list and prompts the user for a command 
    showList(lineList) # call showList to show the current content of the list 

    # show the instructions for the possible commands - [a]dd, [d]elete, e[x]it 
    print('\nType "a" to add an item.') 

    if len(lineList) > 0: # only show the delete instruction if the list has items 
        print('Type "d" to delete an item.') 

    print('Type "x" to exit.') 

    command = input('>') # prompt for a command

    # show the instructions for the possible commands - [a]dd, [d]elete, e[x]it
    if command == 'a': 
        lineList = addToList(FILENAME, lineList) 

    # if "d", call deleteFromList to prompt for item number and delete from list 
    elif command == 'd' and len(lineList) > 0: 
        lineList = deleteFromList(FILENAME, lineList) 

    elif command == 'x': # if "x", break out of the loop to end the program 
        print('Goodbye!') 
        break  
    else: # if anything else, show an error message 
        print('Invalid command.\n')
 
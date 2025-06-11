grid = [[0 for i in range(0,5)] for j in range(0,5) ]

row=0
col=2
grid[row][col]=1


for num in range(2,26):
    new_row=(row-1) % 5
    new_col=(col+1) % 5
    if grid[new_row][new_col]!=0:
        row=(row+1)%5
    else:
        row,col=new_row,new_col
    grid[row][col]=num 

for row in range(0,5):
    for col in range(0,5):
        print(grid[row][col],end="\t")        
    print()


 
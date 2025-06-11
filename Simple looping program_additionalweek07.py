# Simple looping program
import random

count = 1
while True:
    num = random.randint(0, 10)
    if num == 0:
        print("Number ",count, "was ", num)
        break
    elif num == 7:
        print("Lucky 7!")
    else:
        print("Number ",count, "was ", num)
    count += 1
    

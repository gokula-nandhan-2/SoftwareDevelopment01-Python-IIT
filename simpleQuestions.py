# sum 0f numebers
sum = 0
for i in range(1, 11):
    sum += i
print("The sum of numbers from 1 to 10 is:", sum)



# Guessing game
import random
randomNum = random.randint(1, 10)
guess = 0
while guess != randomNum:
    guess = int(input("Guess a number between 1 and 10: "))
    if guess < randomNum:
        print("Too low! Try again.")
    elif guess > randomNum:
        print("Too high! Try again.")
    else:
        print("Congratulations! You've guessed the number:", randomNum)


# number skipper
for i in range(1, 21):
    if i % 2 == 0:
        continue
    else:
        print(i, end=' ')


# Endless input
while True:
    user_input = input("Enter something (type 'exit' to quit): ")
    if user_input == 'exit':
        break
    else:
        print("You entered:", user_input)
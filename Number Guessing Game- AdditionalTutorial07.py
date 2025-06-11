# Number Guessing Game
import random

random_number = random.randint(1, 100)
count = 1
while True:
    guess = int(input("Guess a number between 1 and 100: "))
    if guess == random_number:
        print(guess, "is correct, you win!") 
        print("You got it in", count, " guesses.")
        break
    elif guess < random_number:
        print("Too low!")
    else:
        print("Too high!")
    count += 1
import random
import time

print("Hi! Welcome to the guessing game. I am going to pick a number between 1 and 100.")
time.sleep(3)
print("Picking a number...")
time.sleep(2)
guess = int(input("What is your guess?: "))
correct_number = random.randint(1, 100)
guess_count = 1
while guess != correct_number:
    time.sleep(1)
    guess_count += 1
    if guess < correct_number:
        guess = int(input("Wrong.You need to go higher.What is your guess?: "))
    else:
        guess = int(input("Wrong.You need to go lower.What is your guess?: "))

print(f"Hey, you got the right answer {correct_number} and it took you {guess_count} guessses. ")

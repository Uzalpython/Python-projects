import random

secret_number = random.randint(1, 10)

print("NUMBER GUESSING GAME")
print("I have chosen a number from 1 to 10.")

guess = int(input("Enter your guess: "))

if guess == secret_number:
    print("Congratulations! You guessed correctly.")
elif guess < secret_number:
    print("Your guess is too low.")
else:
    print("Your guess is too high.")

print("The correct number was:", secret_number)
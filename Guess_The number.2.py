# This is a High Low Game
from random import randint
guesses = 1
number = randint(1, 100)

guess = int(input("Guess a number between 1 and 100."))

while guess != number:
    if guess < number:
        print("Your guess was too low.")
        guess = int(input("Guess again."))
        guesses = guesses + 1
    elif guess > number:
        print("Your guess was too high.")
        guess = int(input("Guess again."))
        guesses = guesses + 1

print()
print("*****Congratulation, you guessed the number!*****")
prize_decoration = "*"
print("It only took you", guesses, "guesses!")

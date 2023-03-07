# This is a High Low Game
from random import randint
secret = 7
guesses_allowed = 5

already_guessed = []
guesses_left = guesses_allowed
num_won = 0

guess = ""

while guess != secret and guesses_left >= 1:

    guess = int(input("guess: "))  # replace this with function

    # check that guess is not a duplicate
    if guess in already_guessed:
        print('You already guessed that number! please try again '
              'you *still* have {} guesses left'.format(guesses_left)
        continue
    guesses_left -= 1
    already_guessed.append(guess)

    if guesses_left : continue

while guess != secret:
    if guess < secret:
        print("Your guess was too low.")
        guess = int(input("Guess again."))
        guesses = guesses + 1
    elif guess > secret:
        print("Your guess was too high.")
        guess = int(input("Guess again."))
        guesses = guesses + 1

if guess == secret:
    if guesses_left == guesses_allowed: int = 5
print()
print("*****Congratulation, you guessed the number!*****")
prize_decoration = "*"
print("It only took you", guesses, "guesses!")

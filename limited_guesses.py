import random

guess_range = 50
answer = random.randint(1, guess_range)

guesses_allowed = 10

print("Welcome to the number guessing game!")
print("")

for i in range(guesses_allowed):
    userInput = input("Guess a number between 1 and " + str(guess_range) + ": ")
    guess = int(userInput)

    if guess == answer:
        print("Congratulations! You guessed the correct number. You win!")
        break

    if i == guesses_allowed - 1:
        print("Sorry, you have run out of guesses. You lose!")

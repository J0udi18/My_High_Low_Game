import random


def play_game():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)

    # Keep track of the number of guesses
    num_guesses = 0

    while True:
        # Ask the user to guess the number
        guess = int(input("Guess the number (between 1 and 100): "))
        num_guesses += 1

        # Check if the guess is correct
        if guess == secret_number:
            print(f"Congratulations! You guessed the number in {num_guesses} guesses.")
            break
        elif guess < secret_number:
            print("Higher!")
        else:
            print("Lower!")


if __name__ == '__main__':
    play_game()

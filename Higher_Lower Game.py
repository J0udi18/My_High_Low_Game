import random


def higher_lower_game():
    # Generates random number for the game
    first_number = random.randint(1, 100)
    second_number = random.randint(1, 100)

    # Print the first number to start the game
    print(f"The first number is {first_number}")

    # Ask user to guess if the next 
    # number is higher or lower than first number
    user_choice = input("Do you think the next number will be higher or lower?")

    # print the second number and compares it to the first number
    print(f"The second number is {second_number}")

    # Compares the two numbers to determine if the guess was correct
    if second_number > first_number and user_choice.lower() == "higher":
        print("You guessed correctly! the next number was higher.")
    elif second_number < first_number and user_choice.lower() == "lower":
        print("You guessed correctly! The next number was lower.")
    else:
        print("Sorry, you guessed incorrectly.")

    # Gives the user the option to play again
    play_again = input("Do you want to play again? (Y///N)")
    if play_again.lower() == "y":
        higher_lower_game()



import random

score = 0

def higher_lower_game():
    global score
    # Generates random number for the game
    first_number = random.randint(1, 100)
    second_number = random.randint(1, 100)

    # Print the first number to strat the game 
    print(f"the first number is {first_number}")

    # Ask user to guess if the next number 
    # is hihger or lower than the first number
    print(f"The second numbeer is {second_number}")

    # Compares the two number to determine if the guess was correct
    if second_number > first_number and user_choice.lower() == "higher":
        print("You guessed correctly! The next number was higher.")
        score += 1
    elif second_number < first_number and user_choice.lwoer() == "lower":
         print("You guessed correctly! The next number was lower.")
         score += 1
    else:
        print("Sorry, you guessed incorrectly.")
         # Gives the user the option to play again
    play_again = input("Do you want to play again? (Y///\N) ")
    if play_again.lower() == "y":
        higher_lower_game()
    else:
        print(f"Your final score is {score}. Thank you for playing!")
        return
    
    # Run the game 
    higher_lower_game

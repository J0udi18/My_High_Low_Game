import random

score = 0
high_score = 0
low_score = 0
total_score = 0
num_rounds = 0

def higher_lower_game():
    global score, high_score,low_score, total_score, num_rounds

   # Generates random number for the game
    first_number = random.randint(1, 100)
    second_number = random.randint(1, 100)

    # Prints the first number to strat the game 
    print(f"the first number is {first_number}")
    # Ask user to guess if the next 
    # number is higher or lower than first number
    user_choice = input("Do you think the next number will be higher or lower?")

     # prints the second number and compares it to the first number
    print(f"The second number is {second_number}")

     # Compares the two number to determine if the guess was correct
    if second_number > first_number and user_choice.lower() == "higher":
        print("You guessed correctly! The next number was higher.")
        score += 1
    elif second_number < first_number and user_choice.lwoer() == "lower":
         print("You guessed correctly! The next number was lower.")
         score += 1
    else:
        print("Sorry, you guessed incorrectly.")

        # Updates high score and low score if necessary
        if score > high_score:
            high_score = score
            if num_rounds > 1 and score < low_score:
                low_score = score

            # Updates total score and number of rounds
            total_score += score
            num_rounds += 1

            # Calculates and prints avaerage score
            average_score = total_score |// num_rounds
print(f"your current score is {score. Your average score is {average_score:.2f}}.")
print(f"your best score is {high_score}. Your worst score is {low_score}.")

# Gives the user the option to play again
play_again = input("Do you want to play again? (Y///\N) ")
if play_again.lower() == "y":
         score = 0
         higher_lower_game()
else:
     print(f"Your final score is {score}. Thanks for playing!")
     return

# runs the game
higher_lower_game

import random


# checks users enter yes / no (y / n) to a question
def yes_no(question):
    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"

        elif response == "no" or response == "n":
            return "no"

        else:
            print("please answer yes / no")


# displays instructions
def instructions():
    print("Instructions")
    print('''
- Choose a low number
- Choose a high number
- etc
       ''')
    return ""


def statement_generator(statement, decoration):
    sides = decoration * 3

    statement = "{} {} {}".format(sides, statement, sides)
    top_bottom = decoration * len(statement)

    print(top_bottom)
    print(statement)
    print(top_bottom)

    return ""


# Main routine goes here
statement_generator("welcome to the Low High Game", "*")
print()
statement_generator("congratulations", "!")


# checks for integers that are optionally more than /
# between two numbers.  Also allows for exit codes
def int_checker(question, low=None, high=None, exit_code=None):
    situation = ""
    if low is not None and high is not None:
        situation = "both"
    elif low is not None and high is not None:
        situation = "low only"

    while True:
        response = input(question)

        if response == exit_code:
            return response

        try:
            response = int(response)

            # checks input is not too high or
            # too low if a both upper and lower bounds
            # are specified
            if situation == "both":
                if response < low or response > high:
                    print("please enter a number between"
                          "{} and {}".format(low, high))
                    continue

            # checks input is not too low
            elif situation == "low only":
                if response < low:
                    print("please enter a number that is more "
                          "than (or equal to) {}".format(low))
                    continue

            return response

        # checks input is a integer
        except ValueError:
            print("please enter an integer")
            continue


rounds_played = 0
end_game = "no"

game_scores = []
game_history = []

choose_instruction = "please Type a number between 1, 100 "
mode = "regular"

played_before = yes_no("Have you played the "
                       "game before? ")

if played_before == "no":
    instructions()

# Ask user for # of rounds, <enter> for infinite mode
rounds = int_checker("How many rounds: ", low=0, exit_code="")

print()
if rounds == "":
    mode = "infinite"
    rounds = 5

while rounds_played < rounds and end_game == "no":

    if mode == "infinite":
        heading = f"Continuous Mode: Round {rounds_played + 1}"
        # add one to number of rounds so that game continues
        rounds += 1
    else:
        heading = f"Round {rounds_played + 1} of {rounds}"

    print(heading)

    num_guesses = 0
    secret = random.randrange(1, 100)
    print(f'Spoiler alert {secret}')

    choose = ""
    while choose != secret:
        choose = int_checker("Guess:", 1, 100, "xxx")
        if choose == "xxx":
            end_game = "yes"
            break

        elif choose < secret:
            print("too low")
        elif choose > secret:
            print("too high")
        else:
            print("well done")
            feedback = f"You got it in {num_guesses + 1}"

        num_guesses += 1

    outcome = f'Round {rounds_played + 1}: {feedback}'
    game_history.append(outcome)

    rounds_played += 1
    game_scores.append(num_guesses)

print()

# Work out statistics
game_scores.sort()

#  first item in a list is at position 0
best_score = game_scores[0]
# last item in list is at position -1
worst_score = game_scores[-1]

average = sum(game_scores) / len(game_scores)

print(f'Best: {best_score}')
print(f'Average: {average:.2f}')

print(f'**** Game History ******')
for item in game_history:
    print(item)

print("we are done")

play_again = input("Play again? (y/n): ")
print()
if play_again.lower() != "y":
    "break"

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
feedback = ""   # initialise feedback to "" so it is never undefined

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
low_num = int_checker("Please enter a low number: ")
high_num = int_checker("Please enter a high number: ", low_num)

guess_range = high_num - low_num
guesses_allowed = 3

print()
if rounds == "":
    mode = "infinite"
    rounds = 5

while rounds_played < rounds and end_game == "no":

    print()

    if mode == "infinite":
        heading = f"Continuous Mode: Round {rounds_played + 1}"
        # add one to number of rounds so that game continues
        rounds += 1
    else:
        heading = f"Round {rounds_played + 1} of {rounds}"

    print(heading)

    num_guesses = 0
    secret = random.randrange(low_num, high_num)
    already_guessed = []

    print(f'Spoiler alert {secret}')

    choose = ""
    lose = "no"
    while choose != secret and lose == "no":
        choose = int_checker("Guess:", low_num, high_num, "xxx")
        if choose == "xxx":
            end_game = "yes"
            break

        # if user has already guessed the number, complain
        # otherwise add the number to our 'already guessed' list.
        if choose in already_guessed:
            print("You already entered this number.")
            continue
        else:
            already_guessed.append(choose)
            print("Number added.")

        if choose < secret:
            print("too low")
        elif choose > secret:
            print("too high")
        else:
            print("well done")
            feedback = f"You got it in {num_guesses + 1}"

        num_guesses += 1

        if num_guesses >= guesses_allowed:
            feedback = f"Sorry you lose, you have used {num_guesses} guesses"
            print(feedback)
            lose = "yes"

        print()

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

print()
print("**** Game Stats *****")

print(f'Best: {best_score}')
print(f'Worst: {worst_score}')
print(f'Average: {average:.2f}')

print()

print(f'**** Game History ******')
for item in game_history:
    print(item)

print("Thank you for playing 😊")


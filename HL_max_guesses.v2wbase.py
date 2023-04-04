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


def statement_generator(statement, decoration, lines=None):
    sides = decoration * 3

    statement = "{} {} {}".format(sides, statement, sides)
    top_bottom = decoration * len(statement)

    if lines == 3:
        print(top_bottom)
        print(statement)
        print(top_bottom)
    else:
        print(statement)

    return ""


# checks for integers that are optionally more than /
# between two numbers. Also allows for exit codes
def int_checker(question, low=None, high=None, exit_code=None):
    situation = ""
    if low is not None and high is not None:
        situation = "both"
    elif low is not None and high is None:
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
feedback = ""  # initialise feedback to "" so it is never undefined

game_scores = []
game_history = []

choose_instruction = "please Type a number between 1, 100 "
mode = "regular"

# Main routine goes here
statement_generator("welcome to the Low High Game", "*", 3)
print()

played_before = yes_no("Have you played the "
                       "game before? ")

if played_before == "no":
    instructions()

# Ask user for # of rounds, for infinite mode
rounds = int_checker("How many rounds: ", low=1, exit_code="")
print()
low_num = int_checker("Please enter a low number: ")
high_num = int_checker("Please enter a high number: ", low_num + 1)

guess_range = high_num - low_num
guesses_allowed = 3
max_guesses = int_checker("Enter the maximum number of guesses: ", low=1)

print()
if rounds == "":
    mode = "infinite"
    rounds = 5

while rounds_played < rounds and end_game == "no":

    print()

    if mode == "infinite":
        heading = f"Continuous Mode: Round {rounds_played + 1}"
        # add one

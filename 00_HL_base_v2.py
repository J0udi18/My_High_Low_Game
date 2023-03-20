import random


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
choose_instruction = "please Type a number between 1, 100 "
mode = "regular"

# Ask user for # of rounds, <enter> for infinite mode
rounds = int_checker("How many rounds: ", low=0, exit_code="")

print()
if rounds == "":
    mode = "infinite"
    rounds = 5

while rounds_played <= rounds:

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
            break

        elif choose < secret:
            print("too low")
        elif choose > secret:
            print("too high")
        else:
            print("well done")

        num_guesses += 1

    rounds_played += 1

print()
print("we are done")


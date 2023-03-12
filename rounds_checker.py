import random


# checks how many round had the player played
def check_rounds(round_error=None):
    while True:
        response = input("How many rounds: ")

        rounds_error = "please type either <enter> or an " \
                       "integer that is more than 0\n"

        # If infinite mode not chosen, check response
        # is an integer that is more than 0
        if response != "":
            try:
                response = int(response)

                # If response is too low, go back to
                # start of loop
                if response < 1:
                    print(rounds_error)
                    continue

              except ValueError:
                print(round_error)
                continue
            return response


            # If response is not an integer go back to
            # start of loop
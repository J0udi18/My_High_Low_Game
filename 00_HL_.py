# Hl component 1 _ Get (and Check) user input

# To Do
# Check the lowest is an integer (any integer)
# Check that highest is more than lowest (lower bound only)
# Check that rounds is more than 1 (upper bound only)
# Check that guess is between lowest and highest (
# lower and upper bound)


# Number checking function goes here
def choice_checker(question, low=None, high=None, response=None):
    situation = ""
    if low is not None and high is not None:
        situation = "both"
    elif low is not None and high is not None:
        situation = "low only"

    while True:

        try:
            response = int(input(question))

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
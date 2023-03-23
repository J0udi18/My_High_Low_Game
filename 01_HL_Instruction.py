# Function go here...

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


# Main Routine goes here...
played_before = yes_no("Have you played the "
                       "game before? ")

if played_before == "no":
    instructions()

print("we are done")

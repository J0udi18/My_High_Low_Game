already_guessed = []

count = 0
while count < 4:
    try:
        choose = int(input("Enter a number: "))
        if choose in already_guessed:
            print("You already entered this number.")
        else:
            already_guessed.append(choose)
            print("Number added.")
    except ValueError:
        print("Invalid input. Please enter a number.")

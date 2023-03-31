already_guessed = []

# num_guesses = 0

while True:
    response = input("Guess: ")

    if response == "xxx":
        break

    if response in already_guessed:
        print("You already entered this number.")
        continue
    else:
        already_guessed.append(response)
        # num_guesses += 1

print(f'Number of guesses: {len(already_guessed)}')
# print(f'Num Guesses: {num_guesses}')


# This is a High Low Game
# from random import randint
secret = 7
guesses_allowed = 5

already_guessed = []
guesses_left = guesses_allowed
num_won = 0

guess = ""

while guess != secret and guesses_left >= 1:

    guess = int(input("guess: "))  # replace this with function

    if guess in already_guessed:
        continue
        # check that guess is not a duplicate
        print('You already guessed that number! please try again '
              'you *still* have {} guesses left').format(guesses_left)
        continue
    guesses_left -= 1
    already_guessed.append(guess)

    if guesses_left: continue

while guess != secret:
    if guess < secret:
        print("Your guess was too low.")
        guess = int(input("Guess again."))
        guesses = guesses + 1
    elif guess > secret:
        print("Your guess was too high.")
        guess = int(input('Guess again.'))
        guesses = 'guesses' + 1

if guess == secret:
    if guesses_allowed == guesses_left: int = 5
print()
print("*****Congratulation, you guessed the number!*****")
prize_decoration = "*"
print("It only took you", guesses, "guesses!")

# hard coded for testing purposes - in actual game
# start with empty list and add number of guesses taken
# to it at the end of each round
game_scores = [3, 1, 6, 4, 5, 3]

# Get Stats (goes once game is over)
print("Before sorting...")
print(game_scores)

game_scores.sort()

print("after sorting...")
print(game_scores)

# best score is first item in list (lowest)
best = game_scores[0]

# worst score is last item in list!
worst = game_scores[-1]

# get average
total_scores = sum(game_scores)
average_score = total_scores / len(game_scores)

print()
print("Stats!!")
print(f"Best: {best}")
print(f'Worst: {worst}')
print(f'Average: {average_score:.2f}')



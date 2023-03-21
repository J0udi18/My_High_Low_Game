game_scores = []

# get number of guesses for testing purposes
for item in range(0, 3):
    guesses_needed = int(input("How many guesses: "))
    game_scores.append(guesses_needed)

print(game_scores)

game_scores.sort()

print(game_scores)

#  first item in a list is at position 0
best_score = game_scores[0]
# last item in list is at position -1
worst_score = game_scores[-1]

average = sum(game_scores) / len(game_scores)
print(f'Average: {average:.2f}')

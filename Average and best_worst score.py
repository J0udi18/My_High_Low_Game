import random

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

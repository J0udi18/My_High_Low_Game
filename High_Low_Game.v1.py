import random

gusses = []
cpu_num = random.randint(1, 100)
player_num= int(input("Enter a numver between 1-100: "))
gusses.append(player_num)

while player_num != cpu_num:
    if player_num > cpu_num:
        print("Too high!")
    else:
        print("Too low")
    player_num = int(input("Enter a number between 1-100: "))
    gusses.append(player_num)
else: 
    print("well done!")
    print("It took you i% guesses."% len(gusses))
    print("Here are your guesses: ")
    print(gusses)
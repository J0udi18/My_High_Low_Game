import random

high = 100
low = 1
player_num = int(input("Enter a number between 1-100: "))
cpu_num = random.randint(low, high)
guesses = 1

while player_num != cpu_num:
    print("cpu guess is: %i" % cpu_num)
    if cpu_num > player_num:
        high = cpu_num
    else:
        low = cpu_num
        cpu_num = random.randint(low, high)
    guesses += 1
else:
    print("cpu guess is: %i" % cpu_num)
    print("cpu guesses in %i guesses." % guesses)

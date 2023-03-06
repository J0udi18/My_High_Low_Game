import random


n = int(input("enter a number between 1 and 100: "))
number = random.randint(1, n)
guess = int(input("enter a number between 1 and 100:".format(n)))

while guess != number:
    if guess > number:
        print("your guess was low ")
        guess = int(input("enter a number between 1 and 100: ".format(n)))
        guess += 1

    if guess > number:
        print("Your guess was high")
        guess = int(input("enter a number between 1 and 100: ".format(n)))
play_again = input("press <Enter> to play...").lower()
while play_again == "":
    # increase # of rounds played
    guess += 1

    # print round number
    print()
    print('*** Round #{} ***'.format(guess))
print("you guessed it")
prize_decoration = "*"
print("thank you for playing")

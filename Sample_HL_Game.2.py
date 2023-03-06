import random
import time

n = int(input("enter  number between 1 and: "))
number = random.randint(1,n)
guess = int(input("enter a number between 1 and {}:".format(n)))

while guess != number:
    if guess < number:
        print("your guess was low ")
        time.sleep(1)
        guess = int(input("enter a number between 1 and {}: ".format(n)))


    if guess > number:
        print("Your guess was high")
        time.sleep(1)
        guess = int(input("enter a number between 1 and {}: ".format(n)))

print("you guessed it")

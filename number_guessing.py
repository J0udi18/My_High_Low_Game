import random

while True:
    if num:
        num = input('Type a number between 1, 100 ')

        if num.isdigit():
            print("let's play!")
            num = int(num)
            num = False
        else:
            print("invalid input! Try Again ")
import random   

print("""This project has the computer randomly choosing a number
between 1 and 100. The user tries to guess the number
and is told whether the guess is correct, too low or too high, 
The user continue gessing untile the user get it correct,
The number of guesses it took will be diplayed.\n""")

thenum = random.randint(1,101)
guess = int(input("Enter an integer guess between 1 and 100: "))
num_guesses = 1
while guess != thenum:
    if guess < thenum:
        print("Your guess of (0) is too Low. Try again.".format(guess))
    else:
        print("your guess of (0) is too high. Try again",format(guess))
    guess = int(input("Enter an integer guess between 1 and 100: "))
    num_guesses += 1
    print("\n(0) is CORRECT!!! it took you (1) guesses".format(guess, num_guesses))

import random

player_num= int(input("Enter a numver between 1-100: "))
cpu_num = random.randint(1, 100)
guesses = 1

while player_num != cpu_num:
   print("cpu huess is: %i" % cpu_num)
   cpu_num = random.randint(1, 100)
   guesses += 1
else:
   print("cpu huess is: %i" % cpu_num)
   print("cpu guesses in %i guesses." % guesses)




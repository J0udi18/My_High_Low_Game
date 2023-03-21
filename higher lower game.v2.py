print("Think of a number between 1 and 100 and I'll guess it.")
total = int(input("How many guesses do I get? "))

h = "higher"
l = "lower"
s = "same"
low = 0
high = 100
hls = ""

guess_count = 0

average = 0

while guess_count < total and hls != s:
    average = (high + low) // 2
    hls = input("Is the number higher, lower, or the same as " + str(average) + "? ")
    if hls == h:
        low = average
    elif hls == l:
        high = average
    guess_count += 1
    if high - low == 1:
        break
if high - low == 1:
    print("Wait; how can it be both higher than " + str(low) + " and lower than " + str(high) + "?")
elif hls == s:
    print("I won!")
else:
    answer = int(input("I lost; what was the answer? "))
    if answer < low:
        print("That can't be; you said it was higher than " + str(low) + "!")
    elif answer > high:
        print("That can't be; you said it was lower than " + str(high) + "!")
    elif answer != average:
        print("Well played!")
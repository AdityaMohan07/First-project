from random import randint

n = randint(1, 100)
guess = None
count = 1
while guess != n:
    guess = int(input("Guess the number :"))
    if guess > n:
        print("The number is much smaller")
        print("try again")
        count += 1
    elif guess < n:
        print("The number is much greater")
        print("try again")
        count += 1
    elif guess == n:
        print("Hurray You Got it :) :) ")

print("It took you", count, "guesses")

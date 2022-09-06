# Name: Garrison Brinkerhoff
# Assignment: M02_Programming assignment
# Description: Number between 1 - 10 will be picked and you will have to guess

secret = 6
guess = 0


while guess != secret:
    guess = int(input("Enter a number between 1 and 10: "))

    if guess > secret:
        print("Your number is too high.")
    elif guess < secret:
        print("Your number is too low.")
    else:
        print("You got the number correct.")

# Name: Garrison Brinkerhoff
# Assignment: M02_Programming assignment
# Description: 6.2 loop

guess_me = 7
number = 1

while number != guess_me:
    if number < guess_me:
        print("too low")
        number += 1
    elif number == guess_me:
        print("found it!")
    else:
        print("oops!")
        break
for number in range(number, -1, -1):
    print(number)


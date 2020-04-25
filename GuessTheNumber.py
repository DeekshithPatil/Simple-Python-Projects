
"""Write a programme where the computer randomly generates a number between 0 and 20.
 The user needs to guess what the number is. If the user guesses wrong, tell them their guess is either too high, or too low."""

from random import randrange

value_to_be_guessed = randrange(21)
#print(value_to_be_guessed)

while(1):
    guessed_value = int(input("Enter the guessed number between 0 and 20, inclusive: "))
    if guessed_value == value_to_be_guessed:
        print("Congrats, you got it right")
        break
    elif guessed_value > value_to_be_guessed:
        print("Oops! The value to be guessed is lower than the entered one. Please try again")
    elif guessed_value < value_to_be_guessed:
        print("Uh oh! The value to be guessed is higher than the entered one. Please try again")





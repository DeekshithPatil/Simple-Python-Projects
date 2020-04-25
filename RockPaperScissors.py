"""Make a rock-paper-scissors game where it is the player vs the computer.
The computer’s answer will be randomly generated, while the program will ask the user for their input. """

from random import randrange

values = ['stone', 'paper', 'scissors']

while 1:
    print("******************")
    random_value = randrange(3)
    # print(random_value)
    # print(values[random_value])
    computer_input = values[random_value]
    user_input = input("Enter rock, paper or scissors: ")

    if user_input not in values:
        print("Input error. Please enter either 'rock', 'paper' or 'scissors' only")
    else:
        print("Print computer input is: ")
        print(computer_input)
        if user_input == 'stone':
            if computer_input == 'stone':
                print("It's a draw!")
            elif computer_input == 'paper':
                print("You loose!")
            else:
                print("You win")

        elif user_input == 'paper':
            if computer_input == 'paper':
                print("It's a draw!")
            elif computer_input == 'scissors':
                print("You loose!")
            else:
                print("You win!")
        else:
            if computer_input == 'scissors':
                print("It's a draw!")
            elif computer_input == 'stone':
                print("You loose!")
            else:
                print("You win!")




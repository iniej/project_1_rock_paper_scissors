''' This program lets a user play Rock, Paper, Scissors against the computer.'''
import random

print(' ')
def choice_random():

    keep_going = 'y'

    while keep_going == 'y':
        choice = {1: 'rock', 2: 'paper', 3: 'scissors'}
        num = user_input()
        print('You picked ', choice[num])

        # Generate a random integer between 0 and 4.
        comp = random.randint(1, 3)
        # Use the number as a key to get the choice value.
        print('The computer pick', choice[comp])
        print(' ')
        winner = decider(num, comp)
        print(winner)
        print(' ')
        keep_going = (input("Do you want to play again: enter, 'y', for " + \
        "yes anything else for no "))
        if keep_going != 'y':
            print(' ')
            print('Good Game')

    return winner

def decider (num, comp):
    if num == comp: # If the two numbers are equal, the return "It is a draw"
        return 'It is a draw'

    # If the two numbers are different, then figure out who wins.
    elif num == 1 and comp == 2:
        return 'The computer wins, rock loses to paper'
    elif num == 1 and comp == 3:
         return 'The computer loses, scissors loses to rock'
    elif num == 2 and comp == 3:
         return 'The computer wins, paper loses to scissors'
    elif num == 2 and comp ==1:
        return 'The computer loses, rock loses to paper'
    elif num == 3 and comp ==1:
        return 'The computer wins, scissors loses to rock'
    elif num == 3 and comp == 2:
        return 'The computer loses, paper loses to scissors'
    else:
        return 'Good game'


# Get the player's input.
def user_input():
    # Enter a number.
    number = int(input('Enter a number, 1 = rock, 2 = paper and 3 = scissors: '))
    print(' ')
    while number < 1 or number > 3:
        try:
            print('Please enter a valid number')
            number = int(input('Enter a number, 1 = rock, 2 = paper and 3 = scissors : '))
            print(' ')
        except:
            print('Bad input')
            print(' ')
    return number

def main():

    choice_random()
    print(' ')

# Call the main function.
if __name__ == '__main__':
    main()

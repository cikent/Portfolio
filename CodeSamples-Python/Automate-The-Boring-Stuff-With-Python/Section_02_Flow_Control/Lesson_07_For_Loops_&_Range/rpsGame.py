import random
import sys

print('ROCK, PAPER, SCISSORS')

# These variables keep track of the number of wins, losses, and ties.
wins = 0
losses = 0
ties = 0

while True:  # The main game loop.
    print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
    while True:  # The player input loop.
        print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
        playerMove = input()
        if playerMove == 'q':
            sys.exit()  # Quit the program.
        if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
            break  # Break out of the player input loop.
        print('Type one of r, p, s, or q.')

    # Display what the player chose:
    if playerMove == 'r':
        print('You chose ROCK versus...')
    elif playerMove == 'p':
        print('You chose PAPER versus...')
    elif playerMove == 's':
        print('You chose SCISSORS versus...')

    # Display what the computer chose:
    randomNumber = random.randint(1, 3)
    if randomNumber == 1:
        computerMove = 'r'
        print('The Computer chose ROCK')
    elif randomNumber == 2:
        computerMove = 'p'
        print('The Computer chose PAPER')
    elif randomNumber == 3:
        computerMove = 's'
        print('The Computer chose SCISSORS')

    # Display and record the win/loss/tie:
    if playerMove == computerMove:
        print('It is a tie!')
        ties = ties + 1
    elif playerMove == 'r' and computerMove == 's':
        print('Congrats, you win!')
        wins = wins + 1
    elif playerMove == 'p' and computerMove == 'r':
        print('Congrats, you win!')
        wins = wins + 1
    elif playerMove == 's' and computerMove == 'p':
        print('Congrats, you win!')
        wins = wins + 1
    elif playerMove == 'r' and computerMove == 'p':
        print('Sorry, you lose!')
        losses = losses + 1
    elif playerMove == 'p' and computerMove == 's':
        print('Sorry, you lose!')
        losses = losses + 1
    elif playerMove == 's' and computerMove == 'r':
        print('Sorry, you lose!')
        losses = losses + 1

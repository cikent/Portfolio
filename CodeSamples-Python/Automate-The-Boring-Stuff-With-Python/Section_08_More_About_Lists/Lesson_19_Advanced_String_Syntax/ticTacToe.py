# Create a Tic Tac Toe game!

# Define the Layout of the board as a Dictionary
theBoard = {'top-L': '', 'top-M': '', 'top-R': '', 'mid-L': '', 'mid-M':
 '', 'mid-R': '', 'low-L': '', 'low-M': '', 'low-R': ''}

# Define a Function that allows us to print the Tic Tac Toe board to the screen
def printBroad(board):
    print(board['top-L'] + '|' + board['top-M'] + '|'+ board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|'+ board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|'+ board['low-R'])

# Define a Turn value
turn = 'X'

for i in range(9):
    printBroad(theBoard)
    print('Turn for ' + turn + '. Move on which space?')
    move = input()
    theBoard[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'

# Print to screen the contents of the Board using
printBroad(theBoard)


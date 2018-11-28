import os

# from IPython.display import clear_output
from builtins import input

'''
TODO: Write a function that can print out a board. Set up your board as a list, where each index 1-9 
corresponds with a number on a number pad, so you get a 3 by 3 board representation.
'''


# NOTE: Function to clear the output
def clear():
    os.system('cls')


def display_board(board):
    # clear_output() # HACK: To clear the Notebook
    # print('\n'*10) # HACK: To clear the screen in CLI
    clear()
    print(board[7] + '|' + board[8] + '|' + board[9])
    print(board[4] + '|' + board[5] + '|' + board[6])
    print(board[1] + '|' + board[2] + '|' + board[3])


# TIP: Run your function on a test version of the board list. and make adjustments as necessary.
# test_board = ['#', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X'] * 10
test_board = ['#', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X']
display_board(test_board)


# TODO: Write a function that can take in a player input and assign their marker as 'X' or 'O'
def player_input():
    """
    OUTPUT = (Player 1 marker, Player 2 marker)
    """

    marker = ''

    # while marker != 'X' and marker != '0':
    while not (marker == 'X' or marker == '0'):
        marker = input('Player1: Do you want to be X or O? ').upper()

    if marker == 'X':
        return 'X', 'O'
    else:
        return 'O', 'X'


# TIP: Run the function to make sure it returns the desired output

# player1_marker, player2_marker = player_input()
player_input()

# print('Player 1 marker : ', player1_marker)
# print('Player 2 marker : ', player2_marker)

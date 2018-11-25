import os
from IPython.display import clear_output

# TODO: Write a function that can print out a board. Set up your board as a list, where each index 1-9 corresponds with a number on a number pad, so you get a 3 by 3 board representation.

# NOTE: Function to clear the output
def clear():
  os.system('cls')

def display_board(board):
  # clear_output() # HACK: To clear the Notebook
  # print('\n'*10) # HACK: To clear the screen in CLI
  clear()
  print(board[7]+'|'+board[8]+'|'+board[9])
  print(board[4]+'|'+board[5]+'|'+board[6])
  print(board[1]+'|'+board[2]+'|'+board[3])

# HACK: Run your function on a test version of the board list. and make adjustments as necessary.
test_board = ['#', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X']*10
display_board(test_board)

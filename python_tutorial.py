from audioop import reverse
from cgi import print_environ_usage
from itertools import count
import itertools

from sqlite3 import Row



game = [[2, 1, 1],
        [2, 1, 1],
        [1, 1, 2],]




def win(current_game):
    # Check for horizontal wins

    for row in game:
        print(row)
        if row.count(row[0]) == len(row) and row[0] !=0:  # Check the no, of times row 0 value appears
            print(f"player {row[0]} wins horizontally")


    # Record reverse diagnoal
    digas = []
    cols = reversed(range(len(game)))
    rows = range(len(game))

    # Check for reverse diagnoal wins
    for col, row in zip(cols,rows):
        digas.append(game[row][col])

    if digas.count(digas[0]) == len(digas) and digas[0] !=0:  # Check the no, of times row 0 value appears
        print(f"player {digas[0]} wins diagonally (/)!")
   

    # Checks for diagnoal 

    digas = []
    for ix in range(len(game)):
        digas.append(game[ix][ix])

    if digas.count(digas[0]) == len(digas) and digas[0] !=0: # Check the no, of times row 0 value appears
        print(f"player {digas[0]} wins diagonally (\\)!")

    # Check for vertical wins
    for col in range(len(game)):

        check =[]
        
        for row in game:

            check.append(row[col])
        
        if check.count(check[0]) == len(check) and check[0] != 0 and len(check) >= len(game):
            print(f"player {check[0]} wins vertically (|)!")


def game_board(
        game_ini,player=0,row=0, 
        column=0,just_display=False):           # Avoid immutable object issue by diffrentiating it w/ variable game_ini
  # Hanging indentation

    try:
        print("   0  1  2")
    
        if not just_display:
            game_ini[row][column] = player  # game_ini as game board as "game board" has already been used
            
        for unpack1,unpack2 in enumerate(game_ini):
            print(unpack1,unpack2)
        return game_ini

    except IndexError as e:
        print("error input row/column out of range try 0,1,2 ->",e)

    except Exception as e:
        print("something something wrong ->",e)

play = True

players = [1,2]

while play:
    game = [[0, 0, 0],      # Setting game board
            [0, 0, 0],
            [0, 0, 0],]

    game_won = False
    game = game_board(game,just_display=True)        # Pass in game array as variable 
    player_choice = itertools.cycle([1,2])

    while not game_won:
        current_player = next(player_choice)
        print(f"current player is {[current_player]}")
        column_choice = int(input("what column you want to play? (0,1,2):"))
        row_choice = int(input("what row you want to play? (0,1,2):"))
        game = game_board(game, current_player, row_choice, column_choice)


# game_board(game_board,player=1,row=2,column=2)  # Row out of range
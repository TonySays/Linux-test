from ast import Return
from audioop import reverse
from itertools import count
import itertools

from colorama import Fore, Back, Style

from sqlite3 import Row

def win(current_game):
    # Check for horizontal wins

    def all_same(l):
        if l.count(l[0]) == len(l) and l[0] !=0:
            return True
        else:
            return False

    for row in game:
        print(row)
        if all_same(row):
            print(f"player {row[0]} wins horizontally")
            return True  # Return True then function stops here, otherwise it will keep runing the rest of Code 


    # Record reverse diagnoal
    digas = []
    cols = reversed(range(len(game)))
    rows = range(len(game))

    # Check for reverse diagnoal wins
    for col, row in zip(cols,rows):
        digas.append(game[row][col])

    if all_same(digas):
        print(f"player {digas[0]} wins diagonally (/)!")
        return True
   
    # Checks for diagnoal 
    digas = []
    for ix in range(len(game)):
        digas.append(game[ix][ix])

    if all_same(digas): # Check the no, of times row 0 value appears
        print(f"player {digas[0]} wins diagonally (\\)!")
        return True

    # Check for vertical wins
    for col in range(len(game)):

        check =[]
        
        for row in game:

            check.append(row[col])
        
        if all_same(check):
            print(f"player {check[0]} wins vertically (|)!")
            return True

    return False


def game_board(
        game_ini,player=0,row=0, 
        column=0,just_display=False):           # Avoid immutable object issue by diffrentiating it w/ variable game_ini
  # Hanging indentation

    try:
        if game_ini[row][column]!=0:
            print("This position is occupied, choose another!")
            return game_ini, False
        
        print("   " + "  ".join([str(i) for i in range(len(game_ini))]))
    
        if not just_display:
            game_ini[row][column] = player  # game_ini as game board as "game board" has already been used
            
        for unpack1,unpack2 in enumerate(game_ini):
            colored_row = ""
            for item in unpack2:
                if item == 0:
                    colored_row += "   "
                elif item == 1:
                    colored_row += Fore.GREEN + ' X ' + Style.RESET_ALL
                elif item == 2:
                    colored_row += Fore.MAGENTA + ' 0 ' + Style.RESET_ALL
            print(unpack1,colored_row)

        return game_ini, True

    except IndexError as e:
        print("error input row/column out of range try 0,1,2 ->",e)
        return game_ini, False, 

    except Exception as e:
        print("something something wrong ->",e)
        return game_ini, False

play = True

players = [1,2]

while play:
    game_size = int(input("what size game do you want for tic tac toe? "))
    game = [[0 for i in range(game_size)] for i in range(game_size)]

    game_won = False
    game, _ = game_board(game,just_display=True)        # Pass in game array as variable 
    player_choice = itertools.cycle([1,2])

    while not game_won:
        current_player = next(player_choice)
        print(f"current player is {[current_player]}")
        played = False

        while not played:
            column_choice = int(input(f"what column you want to play? "))
            row_choice = int(input("what row you want to play? "))
            game, played = game_board(game, current_player, row_choice, column_choice)
        
        if win(game):
            game_won = True
            again = input("Game over, want to play again? (y/n) ")
#  My methods
            if again.lower() != "y":
                print("Game End TY! ")
                play = False
            else:
                print("restarting the game now!")

''' Tutorial methods
            if again.lower() == "y":
                print("restarting now")
            elif again.lower() == "n":
                print("game end")
                play = False
            else:
                print("I dont understand")
                play = False
'''         
            
            
# Complete :)


            

# game_board(game_board,player=1,row=2,column=2)  # Row out of range
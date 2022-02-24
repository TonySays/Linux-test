from audioop import reverse
from cgi import print_environ_usage
from itertools import count

from sqlite3 import Row



game = [[2, 1, 1],
        [1, 2, 1],
        [2, 1, 2],]


# Check for diagnoal wins
digas = []
cols = reversed(range(len(game)))
rows = range(len(game))


for col, row in zip(cols,rows):
#   print(col, row)
    digas.append(game[row][col])
print(digas)


digas = []
for ix in range(len(game)):
    digas.append(game[ix][ix])


print(digas)





''' 
# Check for vertical wins


for col in range(len(game)):

    check =[]
    

    for row in game:

        check.append(row[col])
       
        if check.count(check[0]) == len(check) and check[0] != 0 and len(check) >= len(game):

            print(check)

            print("winner!")

'''

'''
# Check for horizontal wins

def win(current_game):
    for row in game:
        print(row)
        if row.count(row[0]) == len(row) and row[0] !=0:  # Check the no, of times row 0 value appears
            print("winner")

win(game)
'''
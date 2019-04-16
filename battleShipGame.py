#Tri (Will) Luong
#Professor Gupta
#COSC 2326
#Battleship game using python

#Global variables
from random import randint


#intializing the board
board = []

#initializing the main board with each values being 0
for x in range(5):
    board.append(["0"] * 5)         #printing 0 5 times to intialize the 2d array with nothing but 0


#displaying the board
def display_board(board):
    for row in board:
        print(''.join(row)) #displaying the board

#starting the game
print("***********************Let's play the battleship*******************************")
display_board(board)

#ship position in row and column
#The key to end the game
def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

#variables to control the game
ship_row = random_row(board)
ship_col = random_col(board)

#player turn
for y in range(4):
    player_row = int(input("Enter your row: "))
    player_col = int(input("Enter your column: "))

#if the player hit the  ship
    if(player_row == ship_row and player_col == ship_col):
        print("*********************You have hit the enemy ship! They have surrendered!*****************")
        print("YOU HAVE WON!")
        break
    else:
#check for out-of-the-board moves
        if(player_row < 0 or player_row > 4) or (player_col < 0 or player_col > 4):
            print("You have made outside of the map")

#make sure for no move repeated
        elif(board[player_row][player_col]=="X"):
            print("You are hitting the same move")

#if the player miss the target, mark the board with an X
        else:
            print("Missed!")
            board[player_row][player_col] = "X"

#print player turn and the board again
        print ("You moved " + str(y+1) + " out of 4.")
        display_board(board)

#if the player reaches the player maximum time, stop the game
    if y >= 3:
        print ("Game Over! You have reached your maximum reach in the game!")

#end of the game

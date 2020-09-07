#
#board
#display board
#play game
#handle turn
#check win
   #check rows
   #check columns
#check tie
#flip player
#
board = ["-", "-", "-",
        "-", "-", "-",
        "-", "-", "-"]

#GLOBAL VARIABLES
#to check if game is over
game_still_going = True

#store winner player
winner = None

#stores current player
current_player = "X"


def display_board():
    #dislpay current board
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])

def handle_turn(player):
    #take position as input from current player 
    valid = False
    #check for valid input
    #if invalid -> keep repeating until valid input
    while not valid:
        pos = input("Choose a position from 1 to 9:")
        if pos in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            pos = int(pos) - 1
            #also check if postion is not already used
            if board[pos] == "-" :
                valid = True
                board[pos] = player
            else:
                print("Invalid position. Try again:")
        else:
            print("Invalid position. Try again:")
    display_board()

def check_if_gameover():
    #checks if game is over either win or tie
    global winner
    check_if_win()
    if winner == None :
        check_if_tie()

def check_if_win():
    #check for winner in rows, columns and diagonals
    check_rows()
    check_col()
    check_diagonals()


def check_rows():
    #if any row has same elements in all postions and is not empty set winner to that element
    #set false to game_still_going to stop further playing
    global winner
    global game_still_going
    i = 0
    while i != 3 :
        if board[i] == board[i+1] == board[i+2] != "-" :
            winner = board[i]
            game_still_going = False
            return
        i += 3
    return
 

def check_col():
     #if any column has same elements in all postions and is not empty set winner to that element
    #set false to game_still_going to stop further playing
    global winner
    global game_still_going
    i = 0
    while i != 3 :
        if board[i] == board[i+3] == board[i+6] != "-" :
            winner = board[i]
            game_still_going = False
            return
        i += 1
    return

def check_diagonals():
     #if any diagonal has same elements in all postions and is not empty set winner to that element
    #set false to game_still_going to stop further playing
    global winner
    global game_still_going
    if board[0] == board[4] == board[8] != "-" :
       winner = board[0]
       game_still_going = False
       return
    elif board[2] == board[4] == board[6] != "-":
        winner = board[2]
        game_still_going = False
        return
    return


def check_if_tie():
    #if all elements are non empty and winner is none then game is a tie
    global winner
    global game_still_going
    i = 0
    for i in range(9) :
        if board[i] == "-" :
            return
    game_still_going = False
    winner = None
    return

def flip_player(player):
    #flip to another player if current player is X then change it to O and vice versa
    global current_player
    if player == "X" :
        current_player = "O"
    elif player == "O" :
        current_player = "X"
    return


def play_game():
    global winner
    global game_still_going
    global current_player
    #dislpay initial board
    display_board()
    #loop stops if game_still_going is set to False
    while game_still_going:
        print(current_player +"'s turn.")
        #take input from player
        handle_turn(current_player)
        #check for win or tie
        check_if_gameover()
        #flip to other player
        flip_player(current_player)
    
    #if game stops print winner
    if winner == "X" or winner == "O":
        print(winner + " won.")
    if winner == None :
        print("Its a tie.")

#start playing game
play_game()
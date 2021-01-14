def display_board(board):
    print(board[1]+'|'+board[2]+'|'+board[3])
    print('-|-|-')
    print(board[4]+'|'+board[5]+'|'+board[6])
    print('-|-|-')
    print(board[7]+'|'+board[8]+'|'+board[9])

board = ['0','1','2','3','4','5','6','7','8','9']
display_board(board)

def player_input():
    
    player_1 = ''
    
    while player_1 != 'X' and player_1 != 'O':
        player_1 = input("Player 1, pick a marker 'X' or 'O': ")
        
        if player_1 == 'X':
            player_2 = 'O'
            print("Player 1: X")
            print("Player 2: O")
            print("Let's start playing!")
            break
        else: 
            player_2 = 'X'
            print("Player 1: O")
            print("Player 2: X")
            print("Let's start playing!")
            break
player_input()

def place_marker(board, position):
    position = int(input("Choose a number between 1 and 9 to mark your position on the board: "))
    if position == 1:
        return board[1] == 'X'
place_marker(board, 1)

import random

def display_board(board):
    print(board[1]+'|'+board[2]+'|'+board[3])
    print('-|-|-')
    print(board[4]+'|'+board[5]+'|'+board[6])
    print('-|-|-')
    print(board[7]+'|'+board[8]+'|'+board[9])
board = ['0','1','2','3','4','5','6','7','8','9']
display_board(board)

def player_input():
    marker = ''
    
    while marker != 'X' and marker != 'O':
        marker = input("Player 1, pick a marker 'X' or 'O': ").upper()
        
        if marker == 'X':
            print("Player 1: X")
            print("Player 2: O")
            return('X', 'O')
        else: 
            print("Player 1: O")
            print("Player 2: X")
            return('O', 'X') 

def place_marker(board, marker, position):
    board[position] = marker

def win_check(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or 
    (board[4] == mark and board[5] == mark and board[6] == mark) or 
    (board[1] == mark and board[2] == mark and board[3] == mark) or 
    (board[7] == mark and board[4] == mark and board[1] == mark) or 
    (board[8] == mark and board[5] == mark and board[2] == mark) or 
    (board[9] == mark and board[6] == mark and board[3] == mark) or 
    (board[7] == mark and board[5] == mark and board[3] == mark) or 
    (board[9] == mark and board[5] == mark and board[1] == mark))
        

def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'

def space_check(board, position):
    return board[position] == ' '

def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True

def player_choice(board):
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose a number 1-9 to mark your position on the board: '))
        
    return position

def replay():
    answer = input('Do you want to play again? Enter yes or no: ').lower()
    return answer =='yes'
                                    
print("Welcome to Tic Tac Toe!")

while True:
    play_board = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first.')

    play_game = input('Are you ready to play? Enter yes or no.')  
    if play_game == 'yes':
        game_on = True
    else:
        game_on = False


    while game_on:
        if turn == 'Player 1':
            display_board(play_board)
            position = player_choice(play_board)
            place_marker(play_board, player1_marker, position)

            if win_check(play_board, player1_marker):
                display_board(play_board)
                print('Congratulations! Player 1 has won the game!')
                game_on = False
            else:
                if full_board_check(play_board):
                    display_board(play_board)
                    print('The game is tied!')
                    game_on = False
                else:
                    turn = 'Player 2'

        else:
            display_board(play_board)
            position = player_choice(play_board)
            place_marker(play_board, player2_marker, position)

            if win_check(play_board, player2_marker):
                display_board(play_board)
                print('Player 2 has won the game!')
                game_on = False
            else:
                if full_board_check(play_board):
                    display_board(play_board)
                    print('The game is tied!')
                    game_on = False
                else:
                    turn = 'Player 1'

    if not replay():
        break
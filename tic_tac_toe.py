# CREATE A GAME OF TIC TAC TOE
    # 2 players should be able to play the game (both sitting at the same computer)
    # The board should be printed out every time a player makes a move
    # You should be able to accept input of the player position and then place a symbol on the board

# Step 1: Write a function that can print out a board. Set up your board as a list, where each index 1-9 corresponds with a number on a number pad, so you get a 3 by 3 board representation.
def display_board(board):
    print('\n'*2)
    print(' '+ board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('~~~~~~~~~~~')
    print(' '+ board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('~~~~~~~~~~~')
    print(' '+ board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('\n'*2)

test_board = ['#','X',' ','X','O','X','O','X','O','X']
#display_board(test_board)

# Step 2: Write a function that can take in a player input and assign their marker as 'X' or 'O'. Think about using while loops to continually ask until you get a correct answer.
def player_input():
    marker = ''
    options = ['X', 'O']
    players = { 1: '', 2: ''}
    while marker not in options:
        result = input('Player 1, would you like to be X or O: ')
        if result.upper() in options:
            marker = result.upper()
    players[1] = marker
    if players[1] == 'X':
        players[2] = 'O'
        print('Ok, Player 1 is X and Player 2 is O')
    else:
        players[2] = 'X'
        print('Ok, Player 1 is O and Player 2 is X')
    return players

#player_input()

# Step 3: Write a function that takes in the board list object, a marker ('X' or 'O'), and a desired position (number 1-9) and assigns it to the board.
def place_marker(board, marker,position):
    board[position] = marker
    return board

#place_marker(test_board, '$', 7)
#display_board(test_board)

# Step 4: Write a function that takes in a board and a mark (X or O) and then checks to see if that mark has won.
def win_check(board, mark):
    winning = [
        [1,2,3],
        [4,5,6],
        [7,8,9],
        [7,4,1],
        [8,5,2],
        [9,6,3],
        [9,5,1],
        [7,5,3]
    ]
    existing_postions = []
    count = 0
    for i in board:
        if i == mark:
           existing_postions.append(count)
           count +=1
        else:
            count +=1
    win = False
    for i in winning: 
        if i[0] in existing_postions and i[1] in existing_postions and i[2] in existing_postions:
            win = True
    return win 

#win_check(test_board, 'X')
#display_board(test_board)

# Step 5: Write a function that uses the random module to randomly decide which player goes first. You may want to lookup random.randint() Return a string of which player went first.
import random

def choose_first():
    rand= random.randint(0,1)
    if rand == 0:
        print('Player 1 will go first')
        return 1
    else:
        print('Player 2 will go first')
        return 2

#choose_first()

# Step 6: Write a function that returns a boolean indicating whether a space on the board is freely available.

def space_check(board, position):
    return board[position] == ' '

#space_check(test_board, 3)

# Step 7: Write a function that checks if the board is full and returns a boolean value. True if full, False otherwise.

def full_board_check(board):
    return ' ' not in board

# full_board_check(test_board)

# Step 8: Write a function that asks for a player's next position (as a number 1-9) and then uses the function from step 6 to check if it's a free position. If it is, then return the position for later use.

def player_choice(board):
    position = int(input('What is your next move: '))
    gone = False
    while not gone:
        if space_check(board, position):
            gone = True
            return position
        else:
            print('Sorry, that space has been taken')


#player_choice(test_board)

# Step 9: Write a function that asks the player if they want to play again and returns a boolean True if they do want to play again.

def replay():
    
    accepted = False
    while accepted == False:
        play_again = input('Do you want to play again? Y/N ')
        if play_again.upper() == 'Y':
            accepted = True
            return True
        elif play_again.upper() == 'N':
            accepted = True
            return False
#replay()

# Step 10: Here comes the hard part! Use while loops and the functions you've made to run the game!
def play():
    print('Welcome to tic tac toe!')
    win = False
    board_full = False
    board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    players = player_input()
    turn = choose_first()
    while not win and not board_full:
        display_board(board)
        print(f'Player {turn}')
        position = player_choice(board)
        marker = players[turn]
        board = place_marker(board,marker,position)
        board_full = full_board_check(board)
        win = win_check(board, marker)
        if turn == 1:
            turn = 2
        else:
            turn = 1
    if win == True:
        if turn == 1:
            winner = 2
        else:
            winner = 1
            print(f'Congratulations Player {winner}- You Won!!!')
            if replay():
               play()
            else:
                print('Thanks for playing!')
    else:
        print('Looks like a tie...')
        if replay():
            play()
        else:
           print('Thanks for playing!')    
        
play()
# CREATE A GAME OF TIC TAC TOE
    # 2 players should be able to play the game (both sitting at the same computer)
    # The board should be printed out every time a player makes a move
    # You should be able to accept input of the player position and then place a symbol on the board

# Step 1: Write a function that can print out a board. Set up your board as a list, where each index 1-9 corresponds with a number on a number pad, so you get a 3 by 3 board representation.
def display_board(board):
    print('\n'*10)
    print(' '+ board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('~~~~~~~~~~~')
    print(' '+ board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('~~~~~~~~~~~')
    print(' '+ board[1] + ' | ' + board[2] + ' | ' + board[3])

test_board = ['#','X','O','X','O','X','O','X','O','X']
display_board(test_board)

# Step 2: Write a function that can take in a player input and assign their marker as 'X' or 'O'. Think about using while loops to continually ask until you get a correct answer.

# Step 3: Write a function that takes in the board list object, a marker ('X' or 'O'), and a desired position (number 1-9) and assigns it to the board.

# Step 4: Write a function that takes in a board and a mark (X or O) and then checks to see if that mark has won.

# Step 5: Write a function that uses the random module to randomly decide which player goes first. You may want to lookup random.randint() Return a string of which player went first.

# Step 6: Write a function that returns a boolean indicating whether a space on the board is freely available.

# Step 7: Write a function that checks if the board is full and returns a boolean value. True if full, False otherwise.

# Step 8: Write a function that asks for a player's next position (as a number 1-9) and then uses the function from step 6 to check if it's a free position. If it is, then return the position for later use.

# Step 9: Write a function that asks the player if they want to play again and returns a boolean True if they do want to play again.

# Step 10: Here comes the hard part! Use while loops and the functions you've made to run the game!
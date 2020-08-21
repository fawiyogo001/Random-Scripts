from IPython.display import clear_output

# displaying board 
def display_board(board):

	clear_output()
	print('	  |   |')
	print('	' + board[7] + ' | ' + board[8] + ' | ' + board[9])
	print('	  |   |')
	print('     ---------------')
	print('	  |   |')
	print('	' + board[4] + ' | ' + board[5] + ' | ' + board[6])
	print('	  |   |')
	print('     ---------------')
	print('	  |   |')
	print('	' + board[1] + ' | ' + board[2] + ' | ' + board[3])
	print('	  |   |')

test_board = ['#','X','O','X','O','X','O','X','O','X']
display_board(test_board)

# player input
def player_input():
	'''
	Output = player 1 marker, player 2 marker
	'''
	marker = ''
	while marker != 'X' and marker != 'O':
		marker = input('Player 1: Choose X or O ').upper()

	if marker == 'X':
		return ('X','O')
	else:
		return('O','X')
# to place a marker in a certain position
def place_marker(board, marker, position):
	board[position] = marker

# winning combinations in tic tac toe
def win_check(board, mark):
	'''
	Possible winning combinations: all rows, all columns, all diagonals
	'''
	# all rows
	return((board[1] == board[2] == board[3] == mark) or 
	(board[4] == board[5] == board[6] == mark) or
	(board[7] == board[8] == board[9] == mark) or

	# all columns
	(board[1] == board[4] == board[7] == mark) or 
	(board[2] == board[5] == board[8] == mark) or
	(board[3] == board[6] == board[9] == mark) or

	# all diagonals
	(board[1] == board[5] == board[9] == mark) or 
	(board[3] == board[5] == board[7] == mark))

# to choose which player goes first
import random

def choose_first():
	flip = random.randint(0, 1)

	if flip == 0:
		return 'Player 1'
	else: 
		return 'Player 2'

# to check space of the board available
def space_check(board, position):
	return board[position] == ' '

# to check if the board is full
def full_board_check(board):
	for i in range(1,10):
		if space_check(board,i):
			return False
	#board is full if true is returned
	return True

# to ask player's choice and use the pervious function to verify vacancy
def player_choice(board):
	position = 0

	while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
		position = int(input('Choose a Position (1 - 9): '))
	return position

# to ask if the players want to play again
def replay():
	return input("Do you want to play again? (Yes/No) ").lower().startswith('y') 

# to run the game and break out of the loop if replay is false
print('Welcome to Tic Tac Toe')

while True:
	# if true the game is played
	the_board = [' '] * 10
	player1_marker, player2_marker = player_input()

	turn = choose_first()
	print(turn + ' will go first')

	play_game = input('Ready to play? (Yes/No) ')
	if play_game.lower()[0] == 'y':
		game_on = True
	else:
		game_on = False 

	while game_on:
		if turn == 'Player 1':
			display_board(the_board)
			position = player_choice(the_board)
			place_marker(the_board, player1_marker, position)

			if win_check(the_board,player1_marker):
				display_board(the_board)
				print('Player 1 won!')
				game_on = False

			else: 
				if full_board_check(the_board):
					display_board(the_board)
					print("Tie!")
					break
				else:
					turn = 'Player 2'
		else:
			display_board(the_board)
			position = player_choice(the_board)
			place_marker(the_board, player2_marker, position)

			if win_check(the_board,player2_marker):
				display_board(the_board)
				print('Player 2 won!')
				game_on = False

			else: 
				if full_board_check(the_board):
					display_board(the_board)
					print("Tie!")
					break
				else:
					turn = 'Player 1'


	# if false the game is stopped
	if not replay():
		break


board = ['' for i in range(10)]

#the input of the player is being translated
# into the position where the player wants his turn
def insertLetter(letter, pos):

	board[pos] = letter

# check if the position is empty or not
# if position is empty return true
def checkSpace(pos):
	return board[pos] == ' '

# prints the board
def printBoard(board):
	print('   |   |   ')
	print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
	print('   |   |   ')
	print('------------')
	print('   |   |   ')
	print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
	print('   |   |   ')
	print('------------')
	print('   |   |   ')
	print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
	print('   |   |   ')

# if the board is full
def isBoardFull(board):
	if board.count(' ') > 1: #check the Board space if there still space
		return False	
	else:
		return True

# conditions to get the winner
def winner(board,letter):
	return ((board[1] == letter and board[2] == letter and board[3] == letter) or
	(board[4] == letter and board[5] == letter and board[6] == letter) or
	(board[7] == letter and board[8] == letter and board[9] == letter) or
	(board[1] == letter and board[4] == letter and board[7] == letter) or
	(board[2] == letter and board[5] == letter and board[8] == letter) or
	(board[3] == letter and board[6] == letter and board[9] == letter) or
	(board[1] == letter and board[5] == letter and board[9] == letter) or
	(board[3] == letter and board[5] == letter and board[7] == letter))



def playerMove():
	run = True
	while run:
		move = input("Select position to enter X between 1 - 9: ")
		# check if the character is valid
		try:
			move = int(move)
			if move > 0  and move < 10:
				# check if the space is empty
				if checkSpace(move):
					run = False
					insertLetter('X', move)
				else:
					print('Space is occupied')
			else:
				print('please pick between 1 - 9')

		except:
			print('Please enter only 1 - 9')

def compMove():
	possibleMove = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
	print('possible move', possibleMove)
	move = 0
	# check the possible move
	for let in ['0' , 'X']:
		for i in possibleMove:
			boardCopy = board[:]
			boardCopy[i] = let
			if winner(boardCopy, let):
				move = i
				return move

	checkcorners = []
	for i in possibleMove:
		if i in [1 , 3 , 7 , 9]:
			checkcorners.append(i)

	if len(checkcorners) > 0:
		move = selectRand(checkcorners)
		return move

	if 5 in possibleMove:
		move = 5
		return move

	checkegdes = []
	for i in possibleMove:
		if i in [2, 4, 6, 8]:
			checkegdes.append(i)

	if len(checkegdes) > 0:
		move = selectRand(checkegdes)
		return move

def selectRand(l):
	import random
	ln = len(l)
	r = random.randrange(0,ln)
	return l[r]

def main():
	print('Welcome to the GAME!')
	printBoard(board)

	while not(isBoardFull(board)):
		if not(winner(board, '0')):
			playerMove()
			printBoard(board)
		else:
			print('Sorry you lose! ')
			break

		if not(winner(board, 'X')):
			move = compMove()
			if move == 0:
				print('Tie game')
			else:
				insertLetter('0', move)
				print('Computer placed an 0 on position', move, ':')
				printBoard(board)
		else:
			print('You WIN')
			break

	if isBoardFull(board):
		print('Tie game')

while True:
	x = input('Do you want to play again? (y/n): ')
	if x.lower() == 'y':
		# printBoard(board)
		board = [' ' for x in range(10)]
		print('-'*16)
		main()

	else:
		break
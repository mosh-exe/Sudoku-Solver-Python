'''
	Sudoku Solver 
	Author: Mohammed Shahwan
	This is a text-based Sudoku Solver implemented using 
	the backtracking algorithm.
'''

def printBoard(board):
	'''
		printBoard prints the Sudoku board.

		Args: 
			board (2-D array [][]): The board array is the Sudoku board.
	'''

	for i in range(len(board)):
		if i % 3 == 0 and i != 0:
			print("- - - - - - - - - - - -  ")

		for j in range(len(board[0])):
			if j % 3 == 0 and j !=  0:
				print(" | ", end="")

			if j == 8:
				print(board[i][j])
			else:
				print(str(board[i][j])+" ", end="")


def findEmpty(board):
	'''
		findEmpty finds an empty square in the Sudoku board
		empty square corresponds to a square with a zero.

		Args: 
			board (2-D array [][]): Sudoku board.

		Return:
			index (int): returns the index of an empty square as an int
						 tuple of the form (row, col). 
	'''
	for i in range(len(board)):
		for j in range(len(board[0])):
			if board[i][j] == 0:
				return (i,j) ## (row, col)
		
	return None 


def valid(board, num, pos):
	'''
		valid determines if the number of each square in the Sudoku
		board is a valid entry.

		Args: 
			board (2-D array [][]): Sudoku board.
			num (int): A number to be inserted into a square within the board
			pos (int(i,j)): position of the square we are trying to solve  

		Return:
			True if a square has a valid solution
			False if atleast one of the boxes contains an invalid solution
	'''

	## Check row 
	for i in range(len(board[0])):
		if board[pos[0]][i] == num and pos[1] != i:
			return False

	## Check column
	for i in range(len(board)):
		if board[i][pos[1]] == num and pos[0] != i:
			return False

	## Check box 
	boxX = pos[1] // 3
	boxY = pos[0] // 3

	for i in range(boxY * 3, boxY * 3 + 3):
		for j in range(boxX * 3, boxX * 3 + 3):
			if board[i][j] == num and (i, j) != pos:
				return False

	return True


def solve(board):
	'''
		solve finds a soultion for the Sudoku board recursively
		
		Args: 
			board (2-D array [][]): Sudoku board.

		Return:
			True if the board has a valid solution
			False if the board has not been solved
	'''

	## finding an empty square
	find = findEmpty(board)
	## no empty squares board has been solved
	if not find:
		return True
	## otherwise set position of empty square	
	else:
		row , col = find

	for i in range (1,10):
		if valid(board, i , (row, col)):
			board[row][col] = i

			if solve(board):
				return True

			board[row][col] = 0 

	return False

def main():
	## Sample Sudoku Board
	board = [
			[3,0,6,5,0,8,4,0,0],
			[5,2,0,0,0,0,0,0,0],
			[0,8,7,0,0,0,0,3,1],
			[0,0,3,0,1,0,0,8,0],
			[9,0,0,8,6,3,0,0,5],
			[0,5,0,0,9,0,6,0,0],
			[1,3,0,0,0,0,2,5,0],
			[0,0,0,0,0,0,0,7,4],
			[0,0,5,2,0,6,3,0,0]
	]

	## Program Testing
	print("Initial Sudoku Board")
	print("               ")
	printBoard(board)
	solve(board)
	print("               ")
	print("Solved Sudoku Board")
	print("               ")
	printBoard(board)

main()
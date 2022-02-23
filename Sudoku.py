import pprint, random
from math import floor
from Boards import *
        
# solver.py
def solve(puzzle):
    """
    Aims to solve puzzle with the common backtracking algorithm used for solving sudoku puzzles.
    Input: puzzle
    Return: True if puzzle is solved, False otherwise.
    """
    find = find_empty(puzzle)
    if find:
        row, col = find
    else:
        return True

    for i in range(1,10):
        if valid(puzzle, (row, col), i):
            puzzle[row][col] = i

            if solve(puzzle):
                return True

            puzzle[row][col] = 0

    return False


def valid(puzzle, coordinates, val):
    """
    Inputs: Puzzle, coordinated in the format (row number, column number), and val of the cell
    valid() checks whether the number val, is a valid entry as per sudoku rules: val must be: unique in it's column, row and box
    Return: True if val is valid, False if val not valid
    """

    #Checks if entry in row is valid. Returns False if entry is not valid.
    for element in puzzle[coordinates[0]]:
        if element == val:
            return False

    #Checks if entry in column is valid. Returns False if is not valid.
    for element in puzzle:
        if element[coordinates[1]] == val:
            return False

    #Checks if entry in square region is valid. Returns False if is not valid.
    start_in_row = floor(coordinates[0]/3)*3
    start_in_col = floor(coordinates[1]/3)*3
    end_in_row = start_in_row + 3
    end_in_col = start_in_col + 3

    for cell_in_row in range(start_in_row, end_in_row):
        for cell_in_col in range(start_in_col, end_in_col):
            if puzzle[cell_in_row][cell_in_col] == val:
                return False    

    return True


def find_empty(puzzle):
    """
    Input: Puzzle
    find_empty() sequentially traverses cells by row until the first empty cell is found. An empty cell is one that contains the value 0
    Return: Coordinates of an empty cell in the format (row number, column number)
    """

    for row in range(len(puzzle)):
        for col in range(len(puzzle[row])):
            if puzzle[row][col] == 0:
                return (row, col)

    return None

board = random.choice([board1, board2, board3, board4])

solve(board)
pprint.pprint(board)
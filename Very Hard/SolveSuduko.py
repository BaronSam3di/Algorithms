"""
----- NAME: Solve sudoku -----
# Has a recursive solution 
----- Category: Recursion -----
----- Level : Very Hard -----
------ BRIEF ------


------ Hints ------


------ Complexity ------ 
Time: O() 
Space: O()

------ Recursive Approach ------

------ Iterative Approach ------

"""

####################################################
## Time: O(1) - Assuming the board is a 9X9 size
## Space: O(1) - Assuming the board is a 9X9 size
####################################################

def solveSudoku(board):
    solvePartialSudoku(0,0,board)
    return board

def solvePartialSudoku(row,col,board):
    '''
    Takes in the row and column position and figures out the correct value to place at this position. 
    Recursive calling, It will backtrack if it cannot find the correct position.
    '''
    currentRow = row
    currentCol = col

    if currentCol == len(board[currentRow]):
        # base case 
        currentRow += 1
        currentCol = 0
        if currentRow == len(board):
            return True                         # board is completed

    if board[currentRow][currentCol] == 0:
        return tryDigitsAtPosition(currentRow,currentCol, board)

    return solvePartialSudoku(currentRow, currentCol + 1,board)


def tryDigitsAtPosition(row,col,board):
    for digit in range(1,10):
        if isValidAtPosition(digit, row , col, board):
            board[row][col] = digit                     # Trying a value at this location on the board 
            if solvePartialSudoku(row,col + 1, board):  # If the line above returns true then we try and solve the board
                return True
    
    board[row][col] = 0                                 # If it didn't work, we reset to zero and back track 4 lines
    return False

def isValidAtPosition(value, row, col ,board):
    '''
    Function tells us if the value is valid in a particular position on our sudoku board 
    Need to check if it's valid in the row, column, subgroup 
    '''
    rowIsValid = value not in board[row]                        # Check the row
    columnIsValid = value not in map(lambda r: r[col],board)    # Check the col

    if not rowIsValid or not columnIsValid:
        return False                                            # value is not in a valid position

    # check subgrid constraint
    subgridRowStart = (row // 3) * 3                            # div by 3 for each set of 9 squares
    subgridColStart = (col // 3) * 3
    for rowIdx in range(3):                                     
        for colIdx in range(3):
            rowToCheck = subgridRowStart + rowIdx
            colToCheck = subgridColStart + colIdx
            existingValue = board[rowToCheck][colToCheck]

            if existingValue == value:                          # if the value is in a 9x9 subgrid then we cannot add it
                return False

    return True
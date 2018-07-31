import pandas as pd
import numpy as np
from SudokuClass import Sudoku

def takeInput(src='puzzles/medium1.xlsx'):
    """
        Create an inputBoard array.
        args:
            src(str): source of excel file
        returns:
            inputBoard(np.array) of size (9,9): Each element is a number in sudoku,
            0 represents empty cells
    """
    given=pd.read_excel(src)
    inputBoard=np.ones((9,9))
    for i in range (9):
        inputBoard[:,i]=np.array(given[i])
    return inputBoard

inputBoard=takeInput()
sudoku=Sudoku(inputBoard)

while(not sudoku.isSolved()):
    sudoku.iterate()

sudoku.printBoard()
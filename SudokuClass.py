from Classes import Cell,CellContainer

class Sudoku(object):
    def __init__(self,inputBoard):
        """
            Take input as np.array and create corresponding container units
            (rows,columns,3*3 squares)
        """
        self.cells=[[Cell(inputBoard[i,j] )for j in range (9)] for i in range (9)]
        
        self.rows=[CellContainer() for i in range (9)]
        for i in range (9):
            for j in range (9):
                self.rows[i].setElement(j, self.cells[i][j] )
 
        self.columns=[CellContainer() for i in range (9)]
        for i in range (9):
            for j in range (9):
                self.columns[j].setElement(i, self.cells[i][j] )
        
        self.squares=[CellContainer() for i in range (9)]
        for i in range (3):
            for j in range (3):
                for k in range (3):
                    for l in range (3):
                        self.squares[3*i+j].setElement(3*k+l, self.cells[3*i+k][3*j+l] )
        
        for i in range (9):
            for j in range (9):
                a=self.rows[i].missingValues
                b=self.columns[j].missingValues
                c=self.squares[i/3*3+j/3].missingValues
                d=list(set(a) & set(b) & set(c))
                self.cells[i][j].addMissingValues(d)

    def printBoard(self):
        """
            Helper function to print the board.
        """
        print "---------------------------------------"
        for j in range (3):
            print "---------------------------------------"
            print "|",self.cells[j][0], "|",self.cells[j][1],"|",self.cells[j][2],"||",self.cells[j][3],"|",self.cells[j][4],"|",\
                self.cells[j][5],"||",self.cells[j][6],"|",self.cells[j][7],"|"\
                   ,self.cells[j][8],"|"
            
        print "---------------------------------------"
        for j in range (3,6):
            print "---------------------------------------"
            print "|",self.cells[j][0], "|",self.cells[j][1],"|",self.cells[j][2],"||",self.cells[j][3],"|",self.cells[j][4],"|",\
                self.cells[j][5],"||",self.cells[j][6],"|",self.cells[j][7],"|"\
                   ,self.cells[j][8],"|"
            
        print "---------------------------------------"
        for j in range (6,9):
            print "---------------------------------------"
            print "|",self.cells[j][0], "|",self.cells[j][1],"|",self.cells[j][2],"||",self.cells[j][3],"|",self.cells[j][4],"|",\
                self.cells[j][5],"||",self.cells[j][6],"|",self.cells[j][7],"|"\
                   ,self.cells[j][8],"|"
        print "---------------------------------------"
        print "---------------------------------------"
    
    def refresh(self):
        """
            Refresh the board by replacing cells with only one missing values 
            with their values
        """
        for i in range (9):
            for j in range (9):
                d=self.cells[i][j].missingValues
                if len(d)==1:
                    self.cells[i][j].setValue(d[0])
    
    def iterate(self):
        """
            One iteration cycle of the sudoku board. Refresh each container and
            overall board
        """
        for i in range(9):
            self.rows[i].refresh()
        for i in range(9):
            self.columns[i].refresh()
        for i in range(9):
            self.squares[i].refresh()
        self.refresh()
    
    def isSolved(self):
        """
            Return 1 if the board does not have any empty slots.
        """
        for i in range (9):
            for j in range (9):
                if self.cells[i][j].value==0:
                    return 0
        return 1
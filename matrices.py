def add(matrix_a, matrix_b):
    """Returns a new matrix that is the sum of the provided matrices"""
    if matrix_a.rows() != matrix_b.rows() or matrix_a.columns() != matrix_b.columns():
        raise ValueError("Matrix A and B must have identical dimensions")

    new_matrix = []

    for i in range(matrix_a.rows()):
        new_matrix.append([])
        for j in range(matrix_a.columns()):
            new_matrix[i].append(matrix_a.elem(i,j) + matrix_b.elem(i,j))
    
    return Matrix(new_matrix)
#end add

def scale(matrix, k):
    """Return a new matrix that is scaled from the original by k"""
    new_matrix = []
    for i in range(matrix.rows()):
        new_matrix.append([])
        for j in range(matrix.columns()):
            new_matrix[i].append(matrix.elem(i,j) * k)
    
    return Matrix(new_matrix)
#end scale

def multiply(matrix_a,matrix_b):       
    def multiply_list_items(*args):
        """Multiplies two lists item by item, returning the resulting list"""
        output_list = []
        for i in range(len(args[0])):
            output_list.append(args[0][i] * args[1][i])
        return output_list
    #end intern multiply_list_items

    """Returns the product of two matrices"""
    if matrix_a.columns != matrix_b.rows(): 
        raise ValueError("Matrix A must have as many columns as Matrix B has rows.")

    new_matrix = []
    for i in range(matrix_a.rows()):
        new_matrix.append([])
        for j in range(matrix_b.columns):
            new_matrix[i].append(
                sum(
                    multiply_list_items(
                        matrix_a.get_row(i), matrix_b.get_column(j)
                )))
    
    return Matrix(new_matrix)
#end multiply

class Matrix:
    _matrix = None
    _rows = None
    _columns = None

    #constructor
    def __init__(self, array):
        """Takes a 2d array and stores it as the matrix. Converts 1d array into row vector."""
        if type(array[0]) is list:
            self._matrix = array
        elif len(array) == 1:
            self._matrix = [array]
        else:
            raise ValueError
        
        self._rows = len(self.matrix)
        self._columns = len(self.matrix[0])
    #end constructor

    def elem(self, i, j):
        """Retrieves the element at i x j from the matrix"""
        return self._matrix[i][j]
    #end elem
    
    def rows(self):
        """Returns the number of rows in the matrix"""
        return self._rows
    #end rows
    
    def columns(self):
        """Returns the number of columns in the matrix"""
        return self._columns
    #end columns

    def swap_row(self, i, j):
        """swaps row i with row j"""
        temp_row = self._matrix[i]
        self._matrix[i] = self.matrix[j]
        self._matrix[j] = temp_row
    #end swap_row

    def scale_row(self, row, k):
        """scales the row by k"""
        temp_row = []

        for i in self._matrix[row]:
            temp_row.append(i * k)

        self._matrix[row] = temp_row
    #end scale_row

    def add_rows(self, source_row, dest_row, k=1):
        """Multiplies source row by k then adds to destination row"""
        temp_row = []

        for i in range(self.rows()):
            temp_row.append(self.elem(source_row, i) * k + self.elem(dest_row, i))

        self._matrix[dest_row] = temp_row
    #end add_rows

    def print(self):
        """Prints the matrix to stdout line by line"""
        for line in self._matrix:
            print(line)
    #end print
    
    def make_int(self,row):
        """Makes the specified row into integers."""
        for i in range(self.columns()):
            self._matrix[row][i] = int(self._matrix[row][i])
    #end make_int
    
    def make_int(self):
        """Makes the entire matrix into integers"""
        for i in range(self.rows()):
            for j in range(self.columns()):
                self._matrix[i][j] = int(self._matrix[i][j])
    #end make_int
    
    def get_column(self,col):
        """Returns all numbers in the specified column as a list."""
        column = []
        for row in self._matrix:
            column.append(row[col])
        return column
    #end get_column

    def get_row(self, row):
        """Returns the row as a list"""
        return self._matrix[row]
    #end get_row

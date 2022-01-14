def add(matrix_a, matrix_b):
    """Returns a new matrix that is the sum of the provided matrices"""
    new_matrix = []

    try:
        #populate matrix
        for i in range(len(matrix_a.matrix)):
            new_matrix.append([])
            for j in range(len(matrix_a.matrix[0])):
                new_matrix[i].append(matrix_a.matrix[i][j] + matrix_b.matrix[i][j])
    except IndexError:
        print("Matrices not equal dimensions")
    
    return Matrix(new_matrix)

def scale(matrix, k):
    """Return a new matrix that is scaled from the original by k"""
    new_matrix = []
    for i in range(len(matrix.matrix)):
        new_matrix.append([])
        for j in range(len(matrix.matrix[0])):
            new_matrix[i].append(matrix.matrix[i][j] * k)
    
    return Matrix(new_matrix)

def multiply(matrix_a,matrix_b):       
    def multiply_list_items(*args):
        """Multiplies two lists item by item, returning the resulting list"""
        list = []
        for i in range(len(args[0])):
            list.append(args[0][i] * args[1][i])
        return list

    """Returns the product of two matrices"""
    new_matrix = []
    for i in range(len(matrix_a.matrix)):
        new_matrix.append([])
        for j in range(len(matrix_b.matrix[0])):
            new_matrix[i].append(
                sum(
                    multiply_list_items(
                        matrix_a.matrix[i], matrix_b.get_column(j)
                )))
    
    return Matrix(new_matrix)

class Matrix:
    matrix = []

    def __init__(self, array):
        """Takes a 2d array and stores it as the matrix. Converts 1d array into row vector."""
        if len(array) == 1 and type(array[0]) is not list:
            self.matrix = [array]
        elif type(array[0]) is list:
            self.matrix = array
        else:
            raise ValueError

    def swap_row(self, i,j):
        """swaps row i with row j"""
        temp_row = self.matrix[i]
        self.matrix[i] = self.matrix[j]
        self.matrix[j] = temp_row

    def scale_row(self, row, k):
        """scales the row by k"""
        temp_row = []

        for i in self.matrix[row]:
            temp_row.append(i * k)

        self.matrix[row] = temp_row

    def add_rows(self, source_row, dest_row, k=1):
        """Multiplies source row by k then adds to destination row"""
        temp_row = []

        for i in range(len(self.matrix[source_row])):
            temp_row.append(self.matrix[source_row][i] * k + self.matrix[dest_row][i])

        self.matrix[dest_row] = temp_row

    def print(self):
        """Prints the matrix to stdout line by line"""
        for line in self.matrix:
            print(line)
    
    def make_int(self,row=-1):
        """Makes the specified row into integers. Makes entire matrix integers if no row specified."""
        if row == -1:
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[0])):
                    self.matrix[i][j] = int(self.matrix[i][j])
        else:
            for i in range(len(self.matrix[row])):
                self.matrix[row][i] = int(self.matrix[row][i])
    
    def get_column(self,col):
            column = []
            for row in self.matrix:
                column.append(row[col])
            return column

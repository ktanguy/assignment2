class SparseMatrix:
    def __init__(self, matrixFilePath=None, numRows=None, numCols=None):
        self.data = {}
        if matrixFilePath:
            with open(matrixFilePath, 'r') as f:
                self.rows = int(f.readline().split('=')[1])
                self.cols = int(f.readline().split('=')[1])
                for line in f:
                    row, col, value = map(int, line.strip('()\n').split(','))
                    self.data[(row, col)] = value
        else:
            self.rows = numRows
            self.cols = numCols

    def getElement(self, currRow, currCol):
        return self.data.get((currRow, currCol), 0)

    def setElement(self, currRow, currCol, value):
        self.data[(currRow, currCol)] = value

    def add(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must have the same dimensions for addition")
        result = SparseMatrix(numRows=self.rows, numCols=self.cols)
        for key in set(self.data.keys()).union(other.data.keys()):
            result.data[key] = self.getElement(*key) + other.getElement(*key)
        return result

    def subtract(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must have the same dimensions for subtraction")
        result = SparseMatrix(numRows=self.rows, numCols=self.cols)
        for key in set(self.data.keys()).union(other.data.keys()):
            result.data[key] = self.getElement(*key) - other.getElement(*key)
        return result

    def multiply(self, other):
        if self.cols != other.rows:
            raise ValueError("The number of columns in the first matrix must be equal to the number of rows in the second for multiplication")
        result = SparseMatrix(numRows=self.rows, numCols=other.cols)
        for i in range(self.rows):
            for j in range(other.cols):
                result.data[(i, j)] = sum(self.getElement(i, k) * other.getElement(k, j) for k in range(self.cols))
        return result

# List of file names
file_names = ['easy_sample_02_1.txt', 'easy_sample_02_2.txt', 'easy_sample_02_3.txt', 
              'easy_sample_03_1.txt', 'easy_sample_03_2.txt', 'easy_sample_03_3.txt', 
              'easy_sample_04_1.txt', 'easy_sample_04_2.txt', 'easy_sample_04_3.txt']

# Create a list to store the matrices
matrices = []

# Loop over the file names
for file_name in file_names:
    # Create an instance of the SparseMatrix class from a file
    matrix = SparseMatrix(matrixFilePath=file_name)
    matrices.append(matrix)


    result_add = matrices[0].add(matrices[1])
    result_subtract = matrices[0].subtract(matrices[1])
    if matrices[0].cols == matrices[1].rows:
        result_multiply = matrices[0].multiply(matrices[1])
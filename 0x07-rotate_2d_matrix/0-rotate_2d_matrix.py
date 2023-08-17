#!/usr/bin/python3
# rotate a matrix by 90 degrees

# def rotate_2d_matrix(matrix):

#    reverse the matrix
#    for i in range(len(matrix)):
#        matrix[i].reverse()

# transpose of the matrix
#    for i in range(len(matrix)):
#        for j in range(i, len(matrix)):

# swapping matrix[i][j] and mat[j][i]
#            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

# Function to print the matrix
# def displayMatrix(matrix):

#    for i in range(0, len(matrix)):
#        for j in range(0, len(matrix)):
#            print(matrix[i][j], end=' ')
#        print()

# Driver code
# if __name__ == "__main__":
#    matrix = [[1, 2, 3],
#            [4, 5, 6],
#            [7, 8, 9]]

#!/usr/bin/python3

""" Rotate 2D Matrix 90 Degrees Clockwise"""


def rotate_2d_matrix(matrix):
    """ Function for rotating 2D Matrix 90 degrees clockwise
    Given an n x n 2D matrix, rotate it 90 degrees clockwise.
    - Do not return anything. The matrix must be edited in-place.
    - You can assume the matrix will have 2 dimensions and will not be empty.
    """

    n = len(matrix[0])

    for i in range(n - 1, -1, -1):
        for j in range(0, n):
            matrix[j].append(matrix[i].pop(0))

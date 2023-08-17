#!/usr/bin/python3
# rotate a matrix by 90 degrees

def rotate_2d_matrix(matrix):
    
    # reverse the matrix
    for i in range(len(matrix)):
        matrix[i].reverse()

    # transpose of the matrix
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):

            # swapping matrix[i][j] and mat[j][i]
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

# Function to print the matrix
def displayMatrix(matrix):

    for i in range(0, len(matrix)):
        for j in range(0, len(matrix)):
            print(matrix[i][j], end=' ')
        print()

# Driver code
if __name__ == "__main__":
    matrix = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]

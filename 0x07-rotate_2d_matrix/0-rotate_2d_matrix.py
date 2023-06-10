#!/usr/bin/python3
''' Given an n x n 2D matrix, rotate it 90 degrees clockwise.

Prototype: def rotate_2d_matrix(matrix):
Do not return anything. The matrix must be edited in-place.
You can assume the matrix will have 2 dimensions and will not be empty.
'''


def rotate_2d_matrix(matrix):
    ''' rotate 2d matrix in 90 degree right '''
    row = len(matrix)
    col = len(matrix[0])
    cl = 0
    ro = row - 1
    for i in range(col * row):
        if i % row == 0:
            matrix.append([])
        if ro == -1:
            ro = row - 1
            cl += 1
        matrix[-1].append(matrix[ro][cl])
        if cl == col - 1 and ro >= -1:
            matrix.pop(ro)
        ro -= 1

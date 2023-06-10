#!/usr/bin/python3
''' Given an n x n 2D matrix, rotate it 90 degrees clockwise.

Prototype: def rotate_2d_matrix(matrix):
Do not return anything. The matrix must be edited in-place.
You can assume the matrix will have 2 dimensions and will not be empty.
'''

def rotate_2d_matrix(matrix):
    ''' rotate 2d matrix in 90 degree right '''
    ''' 
    [1,2,3]
    [4,5,6]
    [7,8,9]
    '''
    new = []
    ln = reversed(range(len(matrix)))
    lst = list(zip(*(list(reversed(matrix)))))
    matrix = [list(ls) for ls in lst]
    return matrix

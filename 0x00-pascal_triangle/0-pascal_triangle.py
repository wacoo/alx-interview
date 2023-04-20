#!/usr/bin/python3
''' return alist for integers representing pascal triangle '''
from math import factorial


def pascal_triangle(n):
    ''' returns a a list of lists of rows
    that make up a pascal triangle '''
    triangle = []
    if type(n) is not int or n <= 0:
        return []
    
    for i in range(n):
        lst = []
        for j in range(i+1):
            ls = factorial(i) // (factorial(j) * factorial(i-j))
            lst.append(ls)
        triangle.append(lst)
    return triangle

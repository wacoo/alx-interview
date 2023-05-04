#!/usr/bin/python3

''' In a text file, there is a single character H. Your text editor
can execute only two operations in this file: Copy All and Paste.
Given a number n, write a method that calculates the fewest number
of operations needed to result in exactly n H characters in the file.

Prototype: def minOperations(n)
Returns an integer
If n is impossible to achieve, return 0
Example:

n = 9

H => Copy All => Paste => HH => Paste =>HHH => Copy All =>
Paste => HHHHHH => Paste => HHHHHHHHH

Number of operations: 6

'''


def minOperations(n):
    ''' retuns number of operations needed to
    copy and paste H n times '''
    clipboard = 0
    char = 'H'
    tmp = ''
    ca = 0
    p = 0
    actions = 0
    while len(char) < n:
        if n % len(char) == 0:
            ca += 1
            p += 1
            tmp = char
            char += char
        else:
            p += 1
            char += tmp
    return ca + p

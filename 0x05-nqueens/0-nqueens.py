#!/usr/bin/python3
'''The N queens puzzle is the challenge of placing N non-attacking queens
on an N×N chessboard. Write a program that solves the N queens problem.

Usage: nqueens N
If the user called the program with the wrong number of arguments, print

Usage: nqueens N, followed by a new line, and exit with the status 1
where N must be an integer greater or equal to 4
If N is not an integer, print N must be a number, followed by a new line,
and exit with the status 1
If N is smaller than 4, print N must be at least 4, followed by a new line,
and exit with the status 1
The program should print every possible solution to the problem
One solution per line
Format: see example
You don’t have to print the solutions in a specific order
You are only allowed to import the sys module'''
import sys
from sys import argv

if len(argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

try:
    n = int(argv[1])
except ValueError:
    print('N must be a number')
    exit(1)

if n < 4:
    print('N must be at least 4')
    exit(1)

result = []
q_pos = []  # places to position the queens
stop = False
# loop through the rows
row = 0
col = 0
while row < n:
    goback = False
    # loop through the columns
    while col < n:
        # make sure current position is safe
        safe = True
        for cord in q_pos:
            co = cord[1]
            if(co == col or co + (row-cord[0]) == col or
                    co - (row-cord[0]) == col):
                safe = False
                break

        if not safe:
            if col == n - 1:
                goback = True
                break
            col += 1
            continue

        # position the queens
        poses = [row, col]
        q_pos.append(poses)
        # if it is the last row, add solution and reset
        if row == n - 1:
            result.append(q_pos[:])
            for cord in q_pos:
                if cord[1] < n - 1:
                    row = cord[0]
                    col = cord[1]
            for i in range(n - row):
                q_pos.pop()
            if row == n - 1 and col == n - 1:
                q_pos = []
                stop = True
            row -= 1
            col += 1
        else:
            col = 0
        break
    if stop:
        break
    # if failed: go back to last row
        # and continue from previeous safe column + 1
    if goback:
        row -= 1
        while row >= 0:
            col = q_pos[row][1] + 1
            del q_pos[row]  # remove last  queen position
            if col < n:
                break
            row -= 1
        if row < 0:
            break
        continue
    row += 1

for idx, val in enumerate(result):
    if idx == len(result) - 1:
        print(val)
    else:
        print(val)

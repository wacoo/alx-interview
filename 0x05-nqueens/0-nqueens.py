#!/usr/bin/env python3
''' '''
import sys
from sys import argv

if len(argv) != 2:
    print('Usage: nqueen N')
    sys.exit(1)
elif not argv[1].isdigit():
    print('N must be anumber')
    sys.exit(1)
elif int(argv[1]) < 4:
    print('N must be at least 4')
    sys.exit(1)

N = int(argv[1])
board = [[0] * N for _ in range(N)]


def attack(i, j):
    for k in range(0, N):
        if board[i][k] == 1 or board[k][j] == 1:
            return True

    for k in range(0, N):
        for d in range(0, N):
            if (k + d == i + j) or (k - d == i - j):
                if board[k][d] == 1:
                    return True
    return False


def N_queens(n):
    if n == 0:
        return True
    for i in range(0, N):
        for j in range(0, N):
            if (not(attack(i, j))) and (board[i][j] != 1):
                board[i][j] = 1
                if N_queens(n - 1):
                    return True
                board[i][j] = 0
    return False


N_queens(N)
lst = []

for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            lst.append([i, j])
print(lst)

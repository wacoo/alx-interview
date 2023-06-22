#!/usr/bin/python3
''' return  the perimeter of the island in the grid '''


def island_perimeter(grid):
    ''' return perimeter '''
    perim = 0
    start = True
    end = True
    ni = len(grid)
    for i in range(ni):
        nj = len(grid[i])
        for j in range(nj):
            if grid[i][j] == 1:
                count = 0
                if i == 0:
                    count += 1
                if i == (ni - 1):
                    count += 1
                if j == 0:
                    count += 1
                if j == (nj - 1):
                    count += 1
                if i > 0:
                    if grid[i - 1][j] == 0:
                        count += 1
                if j < (nj - 1):
                    if grid[i][j + 1] == 0:
                        count += 1
                if i < (ni - 1):
                    if grid[i + 1][j] == 0:
                        count += 1
                if j > 0:
                    if grid[i][j - 1] == 0:
                        count += 1
                perim += count
    return perim

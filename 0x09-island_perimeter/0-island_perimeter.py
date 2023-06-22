#!/usr/bin/python3
''' return  the perimeter of the island in the grid '''


def island_perimeter(grid):
    ''' return perimeter '''
    perim = 0
    start = True
    end = True
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                count = 0
                if i == 0:
                    count += 1
                if i == len(grid):
                    count += 1
                if j == 0:
                    count += 1
                if j == len(grid[i]):
                    count += 1
                if grid[i - 1][j] == 0:
                    count += 1
                if grid[i][j + 1] == 0:
                    count += 1
                if grid[i + 1][j] == 0:
                    count += 1
                if grid[i][j - 1] == 0:
                    count += 1
                perim += count
    return perim

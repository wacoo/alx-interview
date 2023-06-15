#!/usr/bin/python3
''' Given a pile of coins of different values, determine the
fewest number of coins needed to meet a given amount total.'''


def makeChange(coins, total):
    ''' return the fewest change a given conis and and total '''
    if total <= 0:
        return 0
    left = total
    count = 0
    cindex = 0
    sorted_coins = sorted(coins, reverse=True)
    n = len(coins)
    while left > 0:
        if cindex >= n:
            return -1
        if left - sorted_coins[cindex] >= 0:
            left -= sorted_coins[cindex]
            count += 1
        else:
            cindex += 1
    return count

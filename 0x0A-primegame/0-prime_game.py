#!/usr/bin/python3
''' Prime game challenge '''


def isWinner(x, nums):
    ''' identify who is the winner '''
    if x < 1 or not nums:
        return None
    m_wins, b_wins = 0, 0

    n = max(nums)
    prime_nos = [True for _ in range(1, n + 1, 1)]
    prime_nos[0] = False
    for i, is_prime in enumerate(prime_nos, 1):
        if i == 1 or not is_prime:
            continue
        for j in range(i + i, n + 1, i):
            prime_nos[j - 1] = False

    for _, n in zip(range(x), nums):
        prime_nos_count = len(list(filter(lambda x: x, prime_nos[0: n])))
        b_wins += prime_nos_count % 2 == 0
        m_wins += prime_nos_count % 2 == 1
    if m_wins == b_wins:
        return None
    return 'Maria' if m_wins > b_wins else 'Ben'

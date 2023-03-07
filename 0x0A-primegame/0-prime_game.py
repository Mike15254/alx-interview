#!/usr/bin/python3
'''
contains prime game solution
'''


def isWinner(x, nums):
    '''
    Returns the name of the winner
    '''
    if len(nums) == 0:
        return 'Ben'
    wins = {'Maria': 0, 'Ben': 0}
    for i in range(x):
        winner = play(nums[i])
        wins[winner] += 1
    if wins['Ben'] > wins['Maria']:
        return 'Ben'
    return 'Maria'


def play(n):
    '''Maria and Ben take turns choosing numbers
    Return:
        winner of current round
    '''
    current = None
    nums = [x for x in range(1, n+1)]
    i = 0
    while i < len(nums):
        num = nums[i]
        if isPrime(num):
            if current is None or current == 'Ben':
                current = 'Maria'
            else:
                current = 'Ben'
            j = 0
            while j < len(nums):
                if nums[j] % num == 0:
                    nums.pop(j)
                else:
                    j += 1
        else:
            i += 1
    # Maria goes first, therefore she never got the chance to choose
    # a prime number making Ben the winner
    if current is None:
        current = 'Ben'
    return current


def isPrime(n):
    '''checks whether a given number is a prime number'''
    if n == 1 or n == 0:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    w = 2

    while i * i <= n:
        if n % i == 0:
            return False
        i += w
        w = 6 - w

    return True

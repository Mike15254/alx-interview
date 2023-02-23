#!/usr/bin/python3
'''
making change solution
'''


def makeChange(coins, total):
    '''
    making change solution function
    '''
    # dynamic programming -> tabulation
    # dp = [total + 1] * (total + 1)
    # dp[0] = 0

    # for a in range(1, total + 1):
    #     for c in coins:
    #         if a - c >= 0:
    #             dp[a] = min(dp[a], 1 + dp[a-c])
    # return dp[total] if dp[total] != total + 1 else -1
    if (total <= 0):
        return 0
    coin_arr = [float('inf') for i in range(total + 1)]
    coin_arr[0] = 0
    for coin in coins:
        for x in range(len(coin_arr)):
            if coin <= x:
                coin_arr[x] = min(coin_arr[x], 1 + coin_arr[x - coin])
    return coin_arr[total] if coin_arr[total] != float('inf') else -1

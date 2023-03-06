def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def generate_primes(limit):
    # This function generates the first prime number less than or equal to a given limit
    for n in range(limit, 1, -1):
        if is_prime(n):
            return n
    return None


def get_winner(n, player, dp):
    # This function determines the winner for a given state of the game
    if (tuple(range(1, n+1)), player) in dp:
        return dp[(tuple(range(1, n+1)), player)]
    if player == 'Maria':
        p = generate_primes(n)
        if p is not None and get_winner(n-p, 'Ben', dp) == 'Maria':
            dp[(tuple(range(1, n+1)), player)] = 'Maria'
            return 'Maria'
        dp[(tuple(range(1, n+1)), player)] = 'Ben'
        return 'Ben'
    else:
        p = generate_primes(n)
        if p is not None and get_winner(n-p, 'Maria', dp) == 'Ben':
            dp[(tuple(range(1, n+1)), player)] = 'Ben'
            return 'Ben'
        dp[(tuple(range(1, n+1)), player)] = 'Maria'
        return 'Maria'


def isWinner(x, nums):
    winners = {'Maria': 0, 'Ben': 0}
    for n in nums:
        dp = {}
        winner = get_winner(n, 'Maria', dp)
        winners[winner] += 1
    if winners['Maria'] > winners['Ben']:
        return 'Maria'
    elif winners['Ben'] > winners['Maria']:
        return 'Ben'
    else:
        return None

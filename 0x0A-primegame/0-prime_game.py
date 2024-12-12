#!/usr/bin/python3


def sieve_of_eratosthenes(max_n):
    """Returns a list of primes up to max_n."""
    sieve = [True] * (max_n + 1)
    sieve[0] = sieve[1] = False  # 0 and 1 are not primes
    for i in range(2, int(max_n**0.5) + 1):
        if sieve[i]:
            for j in range(i * i, max_n + 1, i):
                sieve[j] = False
    primes = [i for i in range(max_n + 1) if sieve[i]]
    return primes, sieve

def isWinner(x, nums):
    """Determines the overall winner."""
    if not nums or x < 1:
        return None

    max_n = max(nums)
    primes, sieve = sieve_of_eratosthenes(max_n)

    # Precompute the number of prime moves for each n
    prime_moves = [0] * (max_n + 1)
    for i in range(1, max_n + 1):
        prime_moves[i] = prime_moves[i - 1] + (1 if sieve[i] else 0)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if prime_moves[n] % 2 == 0:  # Ben wins if even moves
            ben_wins += 1
        else:  # Maria wins if odd moves
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

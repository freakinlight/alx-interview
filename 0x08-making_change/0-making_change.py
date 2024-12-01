#!/usr/bin/python3
"""
Module for solving the coin change problem.
"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given amount total.

    Parameters:
    - coins (list): List of coin denominations available.
    - total (int): The target amount to achieve with the coins.

    Returns:
    - int: Fewest number of coins needed to make the total,
           or -1 if the total cannot be made.
    """
    if total <= 0:
        return 0

    # Initialize a DP array with a large value (infinity substitute)
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: 0 coins needed to make 0 total

    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1

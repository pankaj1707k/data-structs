""" https://leetcode.com/problems/count-all-valid-pickup-and-delivery-options/ """

from math import factorial
from functools import cache

# Approach 1: Using permutations and combinations
def count_orders(n: int) -> int:
    M = 10 ** 9 + 7
    n_fact = factorial(n) % M
    odd_product = 1
    for num in range(1, 2 * n, 2):
        odd_product = (odd_product * num) % M
    return (n_fact * odd_product) % M


# Approach 2: Using dynamic programming
def count_orders_dp(n: int) -> int:
    M = 10 ** 9 + 7

    @cache
    def total_ways(unpicked: int, undelivered: int) -> int:
        if unpicked < 0 or undelivered < 0 or undelivered < unpicked:
            return 0
        if unpicked == 0 and undelivered == 0:
            return 1
        ways_to_pick = unpicked * total_ways(unpicked - 1, undelivered)
        ways_to_deliver = (undelivered - unpicked) * total_ways(
            unpicked, undelivered - 1
        )
        return (ways_to_pick % M + ways_to_deliver % M) % M

    return total_ways(n, n)

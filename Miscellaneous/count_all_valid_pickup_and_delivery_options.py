""" https://leetcode.com/problems/count-all-valid-pickup-and-delivery-options/ """

from math import factorial


def count_orders(n: int) -> int:
    M = 10 ** 9 + 7
    n_fact = factorial(n) % M
    odd_product = 1
    for num in range(1, 2 * n, 2):
        odd_product = (odd_product * num) % M
    return (n_fact * odd_product) % M

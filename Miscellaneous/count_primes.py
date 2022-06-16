""" https://leetcode.com/problems/count-primes/ """

from math import sqrt


class Solution:
    def countPrimes(self, n: int) -> int:
        # Initialize every number as prime
        prime = [True for _ in range(n)]
        limit = int(sqrt(n)) + 1
        for i in range(2, limit):
            if not prime[i]:
                continue
            # mark all multiples of current prime as non-prime
            # multiples less than i*i are already marked by previous primes
            for j in range(i * i, n, i):
                prime[j] = False
        count = 0
        for i in range(2, n):
            if prime[i]:
                count += 1
        return count

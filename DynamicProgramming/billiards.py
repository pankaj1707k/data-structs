""" https://www.codechef.com/LRNDSA07/problems/CDQU5 """

from typing import *

M = 10**9 + 9

memo = [0]*(10**6 + 1)
memo[2] = memo[3] = 1
for i in range(4, 10**6 + 1):
    memo[i] = (memo[i-2] % M + memo[i-3] % M) % M

def scoreWays(x:int)->int:
    return memo[x]

# t = int(input())
# result = []
# for _ in range(t):
#     x = int(input())
#     result.append(scoreWays(x))

# for r in result:
#     print(r)

# ---------------------------------------------------------------------

# Recursive solution: memory limit exceeded OR recursion depth exceeded

# def scoreWays(x:int)->int:
#     memo = {}
#     def solve(n:int)->int:
#         if n in memo:
#             return memo[n]
#         if n == 2 or n == 3:
#             return 1
#         if n < 2:
#             return 0
#         memo[n] = (solve(n-2) % M + solve(n-3) % M) % M
#         return memo[n]
#     return solve(x)


# Bottom up with computing memo for each test case
# TLE: T<=2000 and X<=10**6 => Runs upto 2*(10**9) iterations

# def scoreWays(x:int)->int:
#     if x < 2:
#         return 0
#     if x == 2 or x == 3:
#         return 1
#     memo = [0]*(x+1)
#     memo[2] = memo[3] = 1
#     for i in range(4,x+1):
#         memo[i] = (memo[i-2] % M + memo[i-3] % M) % M
#     return memo[x]

tests = [5, 7, 2, 99999]
for t in tests:
    print(scoreWays(t))
""" https://leetcode.com/problems/arranging-coins/ """

from math import sqrt

# Method 1: O(n)
def arrangeCoins(n: int) -> int:
    s = 0
    k = 0
    i = 1
    while s < n:
        s += i
        k += 1
        i += 1
    if s == n:
        return k
    return k - 1


# Method 2: O(1)
def arrange_coins(n: int) -> int:
    d = 1 + 8 * n
    k = (sqrt(d) - 1) // 2
    return int(k)


# Method 3: O(log(n)) [Binary search]
def arrange_coins_bs(n: int) -> int:
    left = 0
    right = n
    while left <= right:
        mid = (left + right) // 2
        rows = mid * (mid + 1) // 2
        if rows == n:
            return mid
        if rows > n:
            right = mid - 1
        else:
            left = mid + 1
    return right


t = int(input().strip())
result = []
for _ in range(t):
    n = int(input().strip())
    result.append(arrange_coins(n))

for r in result:
    print(r)

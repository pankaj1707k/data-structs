""" https://leetcode.com/problems/n-th-tribonacci-number/ """


def tribonacci(n, memo={}):
    if n in memo:
        return memo[n]
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    memo[n] = (
        tribonacci(n - 1, memo) + tribonacci(n - 2, memo) + tribonacci(n - 3, memo)
    )
    return memo[n]


if __name__ == "__main__":
    n = int(input().strip())
    result = tribonacci(n)
    print(result)

""" https://leetcode.com/problems/fibonacci-number/ """


def fib(n, memo={}):
    if n in memo:
        return memo[n]
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
        return memo[n]


if __name__ == "__main__":
    n = int(input().strip())
    result = fib(n)
    print(result)

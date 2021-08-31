""" https://leetcode.com/problems/climbing-stairs/ """


def climbStairs(n, memo={}):
    if n in memo:
        return memo[n]
    if n == 1:
        return 1
    elif n == 2:
        return 2

    memo[n] = climbStairs(n - 1, memo) + climbStairs(n - 2, memo)
    return memo[n]


if __name__ == "__main__":
    n = int(input().strip())
    result = climbStairs(n)
    print(result)

""" https://www.hackerrank.com/challenges/coin-change/problem """


def getWays(n, c, m, memo={}):
    if (n, m) in memo:
        return memo[(n, m)]

    if n == 0:   # sum is zero
        return 1    # one way -> not to take any number
    if n < 0 or m <= 0:    # sum is negative or number of coins to be used is at-most zero
        return 0

    memo[(n, m)] = getWays(n, c, m - 1) + getWays(n - c[m - 1], c, m)
    # (num of ways to get n with m nums) = (num of ways to get n excluding the m-th coin) + (num of ways to get n including the m-th coin at least once)
    return memo[(n, m)]


def main():
    n, m = list(map(int, input().rstrip().split()))
    c = list(map(int, input().rstrip().split()))
    result = getWays(n, c, m)
    print(result)


if __name__ == "__main__":
    main()

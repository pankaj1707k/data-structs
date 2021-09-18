""" https://www.hackerrank.com/challenges/coin-change/problem """


def getWays(n, c, m, memo={}):
    if (n,m) in memo:
        return memo[(n,m)]
    
    if n == 0:
        return 1
    if n < 0 or m <= 0:
        return 0
    
    memo[(n,m)] = getWays(n, c, m-1) + getWays(n-c[m-1], c, m)
    return memo[(n,m)]


def main():
    n, m = list(map(int, input().rstrip().split()))
    c = list(map(int, input().rstrip().split()))
    result = getWays(n,c,m)
    print(result)


if __name__=='__main__':
    main()
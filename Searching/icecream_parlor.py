""" https://www.hackerrank.com/challenges/icecream-parlor/problem """

from collections import defaultdict


def icecreamParlor(m, arr):
    d = defaultdict(lambda: -1)
    for i in range(len(arr)):
        x = arr[i]
        y = m-x
        j = d[y]    # for visited positions
        if j != -1:
            return [j+1, i+1]
        d[x] = i


if __name__=='__main__':
    t = int(input().strip())
    results = []
    for _ in range(t):
        m = int(input().strip())
        n = int(input().strip())
        costs = list(map(int, input().rstrip().split()))
        results.append(icecreamParlor(m, costs))
    
    for r in results:
        print(r[0], r[1])
""" https://www.hackerrank.com/challenges/pairs/problem """


def pairs(k, arr):
    s = set(arr)
    p = set()
    for v in s:
        w = v + k
        x = v - k
        if w in s:
            temp = frozenset([v, w])
            if temp not in p:
                p.add(temp)
        if x in s:
            temp = frozenset([v, x])
            if temp not in p:
                p.add(temp)

    return len(p)


if __name__ == "__main__":
    n, k = list(map(int, input().rstrip().split()))
    arr = list(map(int, input().rstrip().split()))
    result = pairs(k, arr)
    print(result)

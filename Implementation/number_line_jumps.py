""" https://www.hackerrank.com/challenges/kangaroo/problem """


def kangaroo(x1, v1, x2, v2):
    num = x1-x2
    den = v1-v2
    if x1 <= x2 and v1 < v2:
        return "NO"
    elif x1 < x2 and v1 <= v2:
        return "NO"
    elif (num // den) == (num / den):
        return "YES"
    else:
        return "NO"


x1, v1, x2, v2 = list(map(int, input().rstrip().split()))
print(kangaroo(x1, v1, x2, v2))
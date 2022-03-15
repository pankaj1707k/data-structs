""" https://www.codechef.com/problems/INVYCNT """

import sys

sys.stdin = open("../input.txt", "r")
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    prefix_pairs = 0
    suffix_pairs = 0

    for i in range(n):
        for j in range(i):
            if arr[j] < arr[i]:
                prefix_pairs += 1
        for j in range(i + 1, n):
            if arr[j] < arr[i]:
                suffix_pairs += 1

    ans = (prefix_pairs * ((k * (k - 1)) // 2)) + (suffix_pairs * ((k * (k + 1)) // 2))
    print(ans)

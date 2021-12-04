""" https://www.codechef.com/LRNDSA07/problems/SUBINC """

from typing import *

def countSubarrays(arr:List[int], n:int)->int:
    memo = [1]*n
    for i in range(1,n):
        if arr[i-1] <= arr[i]:
            memo[i] += 1
    return sum(memo)

# t = int(input())
# result = []
# for _ in range(t):
#     n = int(input())
#     arr = list(map(int, input().split()))
#     result.append(countSubarrays(arr,n))

# for r in result:
#     print(r)

tests = [
    [[1,4,2,3], 4],
    [[1], 1]
]
for t in tests:
    print(countSubarrays(t[0], t[1]))
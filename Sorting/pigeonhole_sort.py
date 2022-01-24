""" 
Pigeonhole sort is a non-comparison sort.
Similar to counting sort but uses an intermediate temporary array.
"""

import sys
from typing import List

sys.stdin = open("../input.txt", "r")
input = sys.stdin.readline


def pigeonhole_sort(arr: List[int]):
    minimum = min(arr)
    maximum = max(arr)
    holes = [[] for _ in range(maximum - minimum + 1)]

    for num in arr:
        holes[num - minimum].append(num)

    i = 0
    for hole in holes:
        for num in hole:
            arr[i] = num
            i += 1


nums = list(map(int, input().split()))
pigeonhole_sort(nums)
for num in nums:
    print(num, end=" ")

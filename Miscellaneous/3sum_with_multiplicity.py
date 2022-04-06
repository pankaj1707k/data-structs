""" https://leetcode.com/problems/3sum-with-multiplicity/ """

from typing import *


def three_sum_multi(arr: List[int], target: int) -> int:
    ans = 0
    MOD = 10 ** 9 + 7
    arr.sort()
    n = len(arr)

    for i in range(n):
        sub_target = target - arr[i]
        # Problem reduced to 2sum
        j = i + 1
        k = n - 1
        while j < k:
            if arr[j] + arr[k] < sub_target:
                j += 1
            elif arr[j] + arr[k] > sub_target:
                k -= 1
            elif arr[j] == arr[k]:  # arr[i] + arr[j] == sub_target
                m = k - j + 1
                ans += m * (m - 1) // 2
                # number of ways of choosing 2 items from k-j+1 items
                ans %= MOD
                j += 1
                k -= 1
            else:
                # if arr[j] != arr[k] find frequency of left and right elements
                left_freq = right_freq = 1
                while j + 1 < k and arr[j] == arr[j + 1]:
                    left_freq += 1
                    j += 1
                while k - 1 > j and arr[k] == arr[k - 1]:
                    right_freq += 1
                    k -= 1
                ans += left_freq * right_freq
                ans %= MOD
                j += 1
                k -= 1

    return ans

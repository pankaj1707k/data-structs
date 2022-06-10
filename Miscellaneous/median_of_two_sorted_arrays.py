""" https://leetcode.com/problems/median-of-two-sorted-arrays/ """

from typing import *


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        # Keep A as smaller array and B as larger array
        if len(A) > len(B):
            A, B = B, A
        total = len(A) + len(B)
        half = total // 2
        l, r = 0, len(A) - 1
        while True:
            # mid point of A (portion of overall left half from A)
            i = (l + r) // 2
            # end index for portion of overall left half from B [half-(i+1)-1]
            j = half - i - 2

            A_left = A[i] if i >= 0 else float("-inf")
            A_right = A[i + 1] if i < len(A) - 1 else float("inf")
            B_left = B[j] if j >= 0 else float("-inf")
            B_right = B[j + 1] if j < len(B) - 1 else float("inf")

            # Correct partition
            if A_left <= B_right and B_left <= A_right:
                if total % 2:
                    return min(A_right, B_right)
                return (max(A_left, B_left) + min(A_right, B_right)) / 2
            elif A_left > B_right:
                r = i - 1  # search left half of A
            else:
                l = i + 1  # search right half of A

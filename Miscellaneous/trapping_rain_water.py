""" https://leetcode.com/problems/trapping-rain-water/ """

from typing import List

# Time: O(n), Space: O(n)
def trap(height: List[int]) -> int:
    n = len(height)
    max_left = [0] * n
    max_right = [0] * n

    for i in range(1, n):
        max_left[i] = max(height[i - 1], max_left[i - 1])
        max_right[n - i - 1] = max(height[n - i], max_right[n - i])

    water = 0
    for i in range(1, n - 1):
        quantity = min(max_left[i], max_right[i]) - height[i]
        water += quantity if quantity > 0 else 0

    return water


# Time: O(n), Space: O(1)
def trap_2(height: List[int]) -> int:
    n = len(height)
    max_left = height[0]
    max_right = height[-1]
    left = 0
    right = n - 1
    water = 0
    while left < right:
        if height[left] < height[right]:
            if height[left] > max_left:
                max_left = height[left]
            else:
                water += max_left - height[left]
            left += 1
        else:
            if height[right] > max_right:
                max_right = height[right]
            else:
                water += max_right - height[right]
            right -= 1
    return water


print(trap_2([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))

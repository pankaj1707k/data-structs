""" https://leetcode.com/problems/house-robber/ """

def rob(nums, memo={}):

    if tuple(nums) in memo:
        return memo[tuple(nums)]
    
    if len(nums) == 0:
        return 0
    if len(nums) == 1:
        return nums[0]

    v1 = nums[0] + rob(nums[2:])
    v2 = rob(nums[1:])
    memo[tuple(nums)] = max(v1,v2)
    return memo[tuple(nums)]


nums = list(map(int, input().rstrip().split()))
print(rob(nums))
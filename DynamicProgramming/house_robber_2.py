""" https://leetcode.com/problems/house-robber-ii/ """

def rob(nums, memo={}):

    if tuple(nums) in memo:
        return memo[tuple(nums)]
    
    if len(nums) == 0:
        return 0
    if len(nums) == 1:
        return nums[0]

    v1 = nums[0] + rob(nums[2:], memo)
    v2 = rob(nums[1:], memo)
    memo[tuple(nums)] = max(v1,v2)
    return memo[tuple(nums)]


nums = list(map(int, input().rstrip().split()))
r1 = rob(nums[:len(nums)-1])
r2 = rob(nums[1:])
print(max(r1, r2))
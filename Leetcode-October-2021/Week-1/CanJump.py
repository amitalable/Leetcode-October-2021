# https://leetcode.com/problems/jump-game/
class Solution:
    def canJump(self, nums):
        n = len(nums)
        k = n-1
        for i in range(n-2, -1, -1):
            if nums[i] >= k-i:
                k = i
        return k == 0

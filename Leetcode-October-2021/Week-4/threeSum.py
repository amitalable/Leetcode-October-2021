# https://leetcode.com/problems/3sum
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        result = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j, k = i + 1, len(nums) - 1
            while j < k:
                val = nums[i] + nums[j] + nums[k]
                if val > 0:
                    k -= 1
                elif val < 0:
                    j += 1
                else:
                    result.append([nums[i], nums[j], nums[k]])
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1
                    j += 1
                    k -= 1
        return result

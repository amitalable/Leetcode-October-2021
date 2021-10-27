# https://leetcode.com/problems/sort-colors/
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        # Position where next found '0' value will be moved
        nextZeroPos = 0
        # Position where next found '2' value will be moved
        nextTwoPos = len(nums) - 1
        # Index of currently checking element
        i = 0
        while i <= nextTwoPos:
            if nums[i] == 0:
                nums[i], nums[nextZeroPos] = nums[nextZeroPos], nums[i]
                nextZeroPos += 1
            elif nums[i] == 2:
                # Next line brings some new value from nextTwoPos to i'th position
                nums[i], nums[nextTwoPos] = nums[nextTwoPos], nums[i]
                nextTwoPos -= 1
                # That's why continue is here: to prevent i(ndex) incremention.
                continue
            i += 1

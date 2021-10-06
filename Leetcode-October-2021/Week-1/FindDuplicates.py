# https://leetcode.com/problems/find-all-duplicates-in-an-array
from typing import List, Counter


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        hashMap = Counter(nums)
        l = []
        for k, v in hashMap.items():
            if v != 1:
                l.append(k)
        return l

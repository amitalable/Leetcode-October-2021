from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        hashTable = {}
        for v in nums2:
            while stack and stack[-1] < v:
                k = stack.pop()
                hashTable[k] = v
            stack.append(v)
        return [hashTable.get(v, -1) for v in nums1]


obj = Solution()
x = [4, 1, 2]
y = [1, 3, 4, 2]
print(obj.nextGreaterElement(x, y))

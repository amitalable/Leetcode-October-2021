# Find all subsets of a set.

from typing import Set


class Solution:
    def __init__(self) -> None:
        self.final_set = set()

    def findSubsets(self, i, arr, n, curr_set):
        if i == n:
            self.final_set.add(frozenset(curr_set))
            return

        self.findSubsets(i+1, arr, n,  curr_set)
        curr_set.add(arr[i])
        self.findSubsets(i+1, arr, n,  curr_set)
        curr_set.remove(arr[i])


obj = Solution()
x = set()
obj.findSubsets(0, [1, 2, 3], 3, x)
print(obj.final_set)

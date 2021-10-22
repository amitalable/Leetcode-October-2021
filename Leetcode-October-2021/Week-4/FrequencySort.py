# https://leetcode.com/problems/sort-characters-by-frequency
from typing import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        hashMap = Counter(s)

        s = {k: v for k, v in sorted(
            hashMap.items(), key=lambda item: -item[1])}
        x = ""
        for k, v in s.items():
            x += k*v
        return x

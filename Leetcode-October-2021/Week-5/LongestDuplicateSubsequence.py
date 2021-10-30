# https://leetcode.com/problems/longest-duplicate-substring
class Solution:
    def longestDupSubstring(self, s: str) -> str:
        ans = ''
        j = 1
        for i in range(len(s)):
            longest = s[i:i+j]
            temp = s[i+1:]
            while longest in temp:
                ans = longest
                j += 1
                longest = s[i:i+j]
        return ans

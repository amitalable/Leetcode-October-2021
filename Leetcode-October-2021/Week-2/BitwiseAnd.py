# https://leetcode.com/problems/bitwise-and-of-numbers-range/
class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:

        if n == m or m == 0:
            return m
        elif len(bin(m)) != len(bin(n)):
            return 0
        else:
            pref = 1 << (len(bin(m))-3)
            return pref ^ self.rangeBitwiseAnd(m - pref, n - pref)

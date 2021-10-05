# https://leetcode.com/problems/climbing-stairs/
class Solution:
    def climbStairs(self, n: int) -> int:
        a = 1
        b = 2
        for i in range(2, n):
            c = a+b
            a = b
            b = c
        return b if n > 1 else a

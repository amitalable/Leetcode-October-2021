# https://leetcode.com/problems/guess-number-higher-or-lower/
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l = [i for i in range(1, n+1)]

        def guess(n, x=6):
            if n == x:
                return 0
            elif n > x:
                return -1
            else:
                return 1

        def binarySearch(left, right):
            mid = (left+right)//2
            t = guess(mid)
            if t == 0:
                return mid
            elif t == -1:
                return binarySearch(left, mid-1)
            else:
                return binarySearch(mid+1, right)
        return binarySearch(1, n)


print(Solution().guessNumber(10))

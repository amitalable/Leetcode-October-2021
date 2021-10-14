# https://leetcode.com/problems/perfect-squares/

class Solution:
    def numSquares(self, n: int) -> int:
        # If the n itself is a perfect sqaure then return 1
        squareRootN = int(n ** (1/2))
        if (squareRootN ** 2) == n:
            return 1
        # Compute all the perfect squares less than n
        nums = [1]
        for i in range(2, squareRootN + 1):
            nums.append(i ** 2)

        # Use BFS to calculate the minimum number of nums to add up to n as below -
        """
            Start from level 1 and initialize the nums to be the values at level 1.
            Now goto next nevel and store the sum for every number of previous level with every number of level 1.
            Stop at that level where the sum of any number with any number to level 1 equal to n.
            Return that level.
        """
        currentLevel = nums
        level = 1
        while True:
            nextLevel = set()
            for i in currentLevel:
                for j in nums:
                    if i + j == n:
                        return level + 1
                    elif i + j < n:
                        nextLevel.add(i + j)
            level += 1
            currentLevel = nextLevel

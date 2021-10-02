from typing import List


class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        if not dungeon:
            return 1
        dp = [[10000000] * (len(dungeon[0]) + 1)
              for i in range(len(dungeon)+1)]
        dp[-2][-1], dp[-1][-1], dp[-1][-2] = 1, 1, 1
        for i in range(len(dungeon)-1, -1, -1):
            for j in range(len(dungeon[0])-1, -1, -1):
                # in case dungeon[i][j] is positive and health become negative
                dp[i][j] = max(1, min(dp[i+1][j], dp[i][j+1]) - dungeon[i][j])
        return dp[0][0]

# https://leetcode.com/problems/word-search/

from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.m, self.n = len(board), len(board[0])
        self.word = word
        self.board = board
        self.directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for row in range(self.m):
            for col in range(self.n):
                if board[row][col] == word[0]:
                    if self.dfs((row, col), 0, {(row, col)}):
                        return True
        return False

    def dfs(self, root, depth, visited):
        # we found a solution
        if depth == len(self.word) - 1:
            return True

        # lazy: use shorter variable names
        r, c = root

        # iterate over all neighbours and recurse
        for d in self.directions:
            rn, cn = r + d[0], c + d[1]

            # constraints:
            # 1. within board dimensions
            # 2. not visited before
            # 3. the neighbour letter matches the next letter
            #    in the target string
            if(self.m > rn >= 0 and
               self.n > cn >= 0 and
               (rn, cn) not in visited and
               self.board[rn][cn] == self.word[depth + 1]
               ):
                # going to explore neighbour, add it to visited
                visited.add((rn, cn))
                # recurse now, return if we find a solution
                if self.dfs((rn, cn), depth + 1, visited):
                    return True
                # we did not find the solution, backtrack
                visited.remove((rn, cn))

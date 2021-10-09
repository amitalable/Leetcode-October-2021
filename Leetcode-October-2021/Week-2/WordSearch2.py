# https://leetcode.com/problems/word-search-ii
from collections import defaultdict
class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.isWord = False
    
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        cur_node = self.root
        for l in word:
            cur_node = cur_node.children[l]
        cur_node.isWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m, n = len(board), len(board[0])
        connections = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        trie = Trie()
        for word in words:
            trie.insert(word)
                
        def dfs(cur_board, cur_i, cur_j, cur_node, cur_path):
            if cur_node.isWord:
                ret.append("".join(cur_path))
                cur_node.isWord = False
            for d_i, d_j in connections:
                new_i, new_j = cur_i+d_i, cur_j+d_j
                if 0 <= new_i < m and 0 <= new_j < n and cur_board[new_i][new_j] in cur_node.children:
                    temp = cur_board[new_i][new_j]
                    cur_board[new_i][new_j] = "*"
                    dfs(cur_board, new_i, new_j, cur_node.children[temp], cur_path+[temp])
                    cur_board[new_i][new_j] = temp
            
        ret = []
        for i in range(m):
            for j in range(n):
                if board[i][j] in trie.root.children:
                    temp = board[i][j]
                    board[i][j] = "*"
                    dfs(board, i, j, trie.root.children[temp], [temp])
                    board[i][j] = temp
        return ret

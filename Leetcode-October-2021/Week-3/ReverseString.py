# https://leetcode.com/problems/reverse-words-in-a-string
class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.strip().split()[::-1])


obj = Solution()
print(obj.reverseWords("  Bob    Loves  Alice   "))

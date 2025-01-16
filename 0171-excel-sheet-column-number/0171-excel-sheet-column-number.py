class Solution:
    def titleToNumber(self, s: str) -> int:
        arr = list(s)
        res = 0
        for i in range(len(s)):
            num = ord(s[i]) - 64
            res = res * 26 + num

        return res

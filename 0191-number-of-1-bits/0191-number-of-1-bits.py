class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n > 0:
            mod = n % 2
            res = res * 10 + mod
            n = n // 2
        res = str(res)[::-1]

        c = 0
        for i in res:
            if i == '1':  # Compare the current character, not the entire string
                c += 1

        return c
        
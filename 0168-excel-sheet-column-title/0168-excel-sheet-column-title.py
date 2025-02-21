class Solution:
    def convertToTitle(self, n: int) -> str:
        res = []
        while n>0:
            n -= 1
            rem = n %26
            res.append(chr(rem + 65))
            n = n//26

        return ''.join(res[::-1])


        
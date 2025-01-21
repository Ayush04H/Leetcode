class Solution:
    def reverse(self, x: int) -> int:
        mul = -1 if x < 0 else 1

        x = abs(x)
        res = 0 
        while x > 0:
            res = res*10 + (x%10)
            x= x//10
            if res > pow(2,31) // 10 :
                return 0

        res = mul * res

        return res

        
class Solution:
    def romanToInt(self, s: str) -> int:
        
        dic = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000,
        }

        res = 0
        prev = 0 
        curr = 0 

        for i in range(len(s)):
            curr = dic[s[i]]
            if curr > prev:
                res += curr - 2 * prev
            
            else:
                res += curr
            prev = curr
        return res

            
        
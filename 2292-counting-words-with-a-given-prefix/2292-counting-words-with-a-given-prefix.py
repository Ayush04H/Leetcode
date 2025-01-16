class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        res = 0 
        r = len(pref)
        for i in words:
            if pref == i[:r]:
                res += 1
                
                
        return res
        
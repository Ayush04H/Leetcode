class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m =float('inf')
        p = -float('inf')
        for pr in prices:
            m= min(pr, m)
            p =max(p,pr-m)

        return p
        
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p = 0 
        bp = prices[0]
        n = len(prices)
        for i in range(1,n):
            if bp > prices[i]:
                bp = prices[i]
            p = max(p,prices[i]-bp)

        return p

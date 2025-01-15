class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p = 0 
        bp = prices[0]
        n = len(prices)
        for i in prices[1:]:
            if bp > i:
                bp = i
            p = max(p,i-bp)

        return p
        
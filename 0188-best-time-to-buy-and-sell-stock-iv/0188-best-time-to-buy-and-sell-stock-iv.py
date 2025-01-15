class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        sell = [float('inf')] * k 
        buy = [float('-inf')] * k 

        for p in prices:
            for i in range(k):
                sell[i] = min(sell[i],p - (buy[i-1] if i > 0 else 0))
                buy[i] = max(buy[i],p-sell[i])

        return buy[k-1]
        
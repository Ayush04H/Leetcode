class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sell_f = float('inf')
        buy_f = 0
        sell_s = float('inf')
        buy_s = 0

        for p in prices:
            sell_f = min(sell_f,p)
            buy_f = max(buy_f,p-sell_f)
            sell_s = min(sell_s,p-buy_f)
            buy_s = max(buy_s,p-sell_s)

        return buy_s
        
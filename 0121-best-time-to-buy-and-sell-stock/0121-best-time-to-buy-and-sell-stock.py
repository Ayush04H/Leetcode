class Solution:
    def maxProfit(self, price: List[int]) -> int:
        ans=0 
        b_p=price[0]
        for i in price[1:]:
            if b_p > i:
                b_p=i

            ans=max(ans,i-b_p)
        return ans


        
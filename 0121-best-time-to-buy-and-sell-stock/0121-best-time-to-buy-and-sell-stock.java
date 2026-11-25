class Solution {
    public int maxProfit(int[] prices) {
        int curr_profit = 0;
        int max_profit = 0;

        for (int i = 1; i < prices.length; i++) {
            int daily_diff = prices[i] - prices[i - 1];
            curr_profit = Math.max(0, curr_profit + daily_diff);
            max_profit = Math.max(max_profit, curr_profit);
        }

        return max_profit;
    }
}

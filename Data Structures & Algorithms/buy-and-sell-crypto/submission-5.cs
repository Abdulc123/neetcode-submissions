public class Solution {
    public int MaxProfit(int[] prices) {
        // Buy low sell high
        
        int L = 0;
        int R = 1;
        int maxProfit = 0;

        while (R < prices.Length)
        {
            // If the L is smaller than R, we can gain profit
            if (prices[L] < prices[R])
            {
                int profit = prices[R] - prices[L]; // Sell - Buy
                maxProfit = Math.Max(maxProfit, profit);
                Console.WriteLine($"{prices[L]}, {prices[R]} | Profit = {profit}");
            }
            else 
            {
                // The R price is smaller than our current buy so use that instead when moving forward
                L = R;
            }
            R++;
            
        }


        return maxProfit;
    }
}

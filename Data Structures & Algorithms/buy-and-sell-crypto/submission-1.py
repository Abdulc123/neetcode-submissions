class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_profit = 0
        l = 0 # buy
        r = 1 # sell
        n = len(prices)
        

        while r < n:
            #print(l, r)
            if prices[l] < prices[r]: # if buy is less than sell
                profit = prices[r] - prices[l]
                max_profit = max(max_profit, profit)
            else: # when sell is less than buy 
                l = r
            # sets buy to sell and moves sell up 1
            r += 1
            

        return max(max_profit, 0)
                         

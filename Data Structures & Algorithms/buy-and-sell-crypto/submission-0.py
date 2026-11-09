class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        buy , sell = 0 , 1
        res = 0
        while sell < n:
            if prices[buy] > prices[sell]:
                buy = sell
            else:
                profit = prices[sell] - prices[buy]
                res = max(res,profit)
            sell += 1
        return res
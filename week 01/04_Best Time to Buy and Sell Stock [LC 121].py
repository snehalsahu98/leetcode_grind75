class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # have forgotten the bloody logic -> would have to recall this
        # lets try using sliding window

        profit = 0
        l = 0       

        for r in range (1, len(prices)):
            if prices[l] > prices[r]:
                l = r

            profit = max(profit, prices[r] - prices[l])

        return profit

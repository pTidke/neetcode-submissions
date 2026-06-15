class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        maxprofit=0
        minimum = prices[0]

        for day in range(1, len(prices)):
            profit = prices[day] - minimum

            maxprofit = max(profit,maxprofit)

            if prices[day] < minimum:
                minimum = prices[day]

        return maxprofit
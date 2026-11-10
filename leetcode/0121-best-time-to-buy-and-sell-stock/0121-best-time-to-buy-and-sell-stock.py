class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_profit = 0
        left = 0
        right = 1

        while right < len(prices):

            if prices[right] < prices[left]:
                left = right

            else:
                profit = prices[right] - prices[left]

                if profit > max_profit:
                    max_profit = profit

            right += 1

        return max_profit
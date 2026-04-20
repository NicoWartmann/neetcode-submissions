class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = prices[0] + 1
        highest = 0
        for i in range(len(prices)):
            if prices[i] < lowest:
                lowest = prices[i]
                for j in range(i, len(prices)):
                    if (prices[j] - prices[i]) > highest:
                        highest = prices[j] - prices[i]
        return highest
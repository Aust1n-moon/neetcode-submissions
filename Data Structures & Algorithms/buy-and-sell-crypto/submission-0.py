class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # dynamic sliding window question
        # create a maxres = 0
        # using a for loop for each index, if prices[i] - price at index is > maxres, update maxres
        # return maxres

        maxres = 0

        for i in range(len(prices)):
            j = i + 1

            while j < len(prices):
                profit = prices[j] - prices[i]

                if profit > maxres:
                    maxres = profit
                
                j += 1
            
        return maxres
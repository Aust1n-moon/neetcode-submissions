class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # dynamic sliding window question
        # create a maxres = 0
        # using two pointer, count up all right side for the left pointer, and if res > maxres replace
        # return maxres

        maxres = 0

        l,r = 0, 1

        while r < len(prices):
            if prices[l] < prices[r]:
                res = prices[r] - prices[l]
                maxres = max(res,maxres)
            else:
                l = r
            
            r += 1

        return maxres

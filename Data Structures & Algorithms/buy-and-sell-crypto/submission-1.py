class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        l = 0
        r = l + 1
        res = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                price = prices[r] - prices[l]
                res = max(res, price)
            else:
                l = r
            r +=1
        return res
            
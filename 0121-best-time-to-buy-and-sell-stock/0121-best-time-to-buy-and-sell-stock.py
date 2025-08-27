class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price = float('inf')
        max_profit = 0

        for p in prices:
            min_price = min(min_price, p)      # track lowest price so far
            max_profit = max(max_profit, p - min_price)  # best profit so far

        return max_profit
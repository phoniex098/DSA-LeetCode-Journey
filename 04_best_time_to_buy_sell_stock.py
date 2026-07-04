# Problem: 121. Best Time to Buy and Sell Stock
# Difficulty: Easy

class Solution:
    def maxProfit(self, prices):
        prof = [0]
        mi = prices[0]
        for n in prices:
            if mi >= n:
                mi = n
            else:
                prof.append(n - mi)
        return max(prof)

# Problem: 122. Best Time to Buy and Sell Stock II
# Difficulty: Medium (LeetCode calls it Medium)
# Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

# Pattern: Greedy / Single Pass
# Approach:
# - Track minimum price so far
# - When price goes up, take the profit and reset
# - Sum up all profitable transactions

# Time Complexity: O(n) - single pass through prices
# Space Complexity: O(1) - only 2 variables used

class Solution:
    def maxProfit(self, prices):
        prof = 0
        mi = prices[0]
        for p in prices:
            if p <= mi:
                mi = p
            else:
                prof = prof + p - mi
                mi = p
        return prof


# LeetCode Result:
# Runtime: 3ms (Beats 60.78%)
# Memory: 20.20 MB (Beats 97.59%)

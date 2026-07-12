# Problem: 347. Top K Frequent Elements
# Difficulty: MEDIUM
# Link: https://leetcode.com/problems/top-k-frequent-elements/

# Pattern: HashMap for Counting + Sorting
# Approach:
# - Count frequency of each number using HashMap
# - Sort dictionary keys by their frequency (descending)
# - Return top k keys

# Time Complexity: O(n log n) - dominated by sorting
# Space Complexity: O(n) - dict storing frequencies

class Solution:
    def topKFrequent(self, nums, k):
        d = {}
        for n in nums:
            if n not in d:
                d[n] = 1
            else:
                d[n] = d[n] + 1
        return list(sorted(d, key=d.get, reverse=True))[:k]


# LeetCode Result:
# Runtime: 7ms (Beats 52.03%)
# Memory: 22.65 MB (Beats 94.32%)

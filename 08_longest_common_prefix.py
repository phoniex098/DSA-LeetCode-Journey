# Problem: 14. Longest Common Prefix
# Difficulty: Easy
# Link: https://leetcode.com/problems/longest-common-prefix/

# Pattern: String Comparison / Vertical Scanning
# Approach:
# - Find shortest string (limits max prefix length)
# - Compare each character of first string with others
# - Track longest matching prefix length

# Time Complexity: O(n * m)
#   where n = number of strings, m = length of shortest string
# Space Complexity: O(1) - only counters used

class Solution:
    def longestCommonPrefix(self, strs):
        n = len(strs)
        mn = len(strs[0])
        ko = min(strs, key=len)
        k = 0
        for i in range(1, n):
            for j in range(len(ko)):
                if strs[0][j] == strs[i][j]:
                    k = k + 1
                else:
                    break
            if mn >= k:
                mn = k
            k = 0
        if mn == 0:
            return ""
        return strs[0][:mn]


# LeetCode Result:
# Runtime: 0ms (Beats 100.00%)
# Memory: 19.24 MB (Beats 72.28%)

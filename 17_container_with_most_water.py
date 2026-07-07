# Problem: 11. Container With Most Water
# Difficulty: MEDIUM
# Link: https://leetcode.com/problems/container-with-most-water/

# Pattern: Two Pointers (Converging)
# Approach:
# - Start with widest container (left=0, right=n-1)
# - Calculate area = min(height[l], height[r]) * (r - l)
# - Move the pointer at the SHORTER height
#   (Moving taller one only reduces width, doesn't help)

# Why move shorter pointer:
# - Area is limited by SHORTER wall
# - Moving shorter has CHANCE of finding taller wall
# - Moving taller only reduces width, area can only decrease

# Time Complexity: O(n) - each pointer moves at most n times
# Space Complexity: O(1) - only variables

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        m = 0
        while l < r:
            if height[l] < height[r]:
                s = height[l]
            else:
                s = height[r]
            area = (r - l) * s
            m = max(area, m)
            if s == height[r]:
                r = r - 1
            else:
                l = l + 1
        return m

# LeetCode Result:
# Runtime: 50ms (Beats 86.84%)
# Memory: 29.86 MB (Beats 5.24%)

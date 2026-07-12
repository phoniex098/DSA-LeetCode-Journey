# Problem: 162. Find Peak Element
# Difficulty: MEDIUM
# Link: https://leetcode.com/problems/find-peak-element/

# Pattern: Binary Search (on unsorted array — using local property)
# STATUS: ❌ HINT from LeetCode on Jul 10 - MUST RE-SOLVE SOLO Jul 11

# KEY INSIGHT (huge concept):
# Binary search does NOT require a sorted array.
# It requires a DECIDABLE half-condition — a way to know
# which half MUST contain the answer just from local info.

# Here: peak = element greater than both neighbors.
# By comparing nums[m] and nums[m+1]:
# - If nums[m] < nums[m+1] → climbing up → peak exists to the RIGHT
# - Else                   → going down  → peak exists at m OR LEFT

# Time Complexity: O(log n)
# Space Complexity: O(1)

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] < nums[m + 1]:
                l = m + 1
            else:
                r = m
        return l

# LeetCode Result:
# Runtime: 0ms (Beats 100.00%)
# Memory: 19.34 MB (Beats 39.15%)

# NOTE: Approach was hinted by LeetCode. Re-solve solo Jul 11.

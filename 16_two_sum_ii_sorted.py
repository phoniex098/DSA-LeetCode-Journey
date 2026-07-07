# Problem: 167. Two Sum II - Input Array Is Sorted
# Difficulty: MEDIUM (but Easy given pattern)
# Link: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

# Pattern: Two Pointers (Converging) - SORTED ARRAY
# Approach:
# - Left pointer at start, right pointer at end
# - If sum too small → move left right (increase)
# - If sum too big → move right left (decrease)
# - If sum matches → return indices (1-indexed)

# Key Insight:
# The array is SORTED. Use Two Pointers instead of HashMap.
# This gives O(1) space instead of O(n).

# Time Complexity: O(n) - each pointer moves at most n times
# Space Complexity: O(1) - only two variables

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        f = 0
        l = len(numbers) - 1
        while l > f:
            s = numbers[f] + numbers[l]
            if s == target:
                return (f + 1, l + 1)
            elif s > target:
                l = l - 1
            else:
                f = f + 1


# ═══════════════════════════════════════════
# FAILED ATTEMPT (Learning Record)
# ═══════════════════════════════════════════
# ❌ First attempt: O(n³) using nested loops with list.index()
# Runtime: 5364ms (Beats 7.30%)
# Lesson: "Sorted Array" in problem name = HUGE HINT for Two Pointers
# Don't default to HashMap when array is sorted


# LeetCode Result (Correct):
# Runtime: 3ms (Beats 80.19%)
# Memory: 20.57 MB (Beats 35.74%)

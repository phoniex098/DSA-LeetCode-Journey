# Problem: 128. Longest Consecutive Sequence
# Difficulty: MEDIUM
# Link: https://leetcode.com/problems/longest-consecutive-sequence/

# Pattern: HashSet + Sequence Detection
# Note: Watched NeetCode video for approach
# Need to re-solve on July 9 without help

# Approach:
# 1. Convert nums to a set for O(1) lookups
# 2. For each number, check if it's a sequence START
#    (a number is a start if (n-1) is NOT in the set)
# 3. From each start, count how long the sequence goes
# 4. Track the maximum length

# Why O(n) despite while loop:
# Each number is visited at most twice across entire algorithm
# (Once for start-check, once as part of some sequence)

# Time Complexity: O(n)
# Space Complexity: O(n) - for the set

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        k = 0
        nu = set(nums)
        for n in nu:
            if n - 1 not in nu:
                l = 0
                while n + l in nu:
                    l = l + 1
                k = max(l, k)
        return k


# LeetCode Result:
# Runtime: 48ms (Beats 64.21%)
# Memory: 36.51 MB (Beats 66.55%)

# Problem: 643. Maximum Average Subarray I
# Difficulty: EASY
# Link: https://leetcode.com/problems/maximum-average-subarray-i/

# Pattern: Sliding Window (Fixed Size)
# Approach:
# - Maintain running sum of window of size k
# - When window reaches size k, record max
# - Slide: add nums[right], subtract nums[left], move left forward

# Why keep track of SUM not average:
# - Division inside loop is slow
# - Divide once at the end: return max_sum / k

# Time Complexity: O(n) - single pass
# Space Complexity: O(1) - only variables

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        m = -float('inf')
        left = 0
        l = 0
        for right in range(len(nums)):
            l = l + nums[right]
            if right + 1 - left == k:
                m = max(m, l)
                l = l - nums[left]
                left = left + 1
        return m / k

# LeetCode Result:
# Runtime: 99ms (Beats 12.09%)
# Memory: 29.31 MB (Beats 16.52%)
# Note: Runtime % is Python noise. Algorithm is optimal O(n).

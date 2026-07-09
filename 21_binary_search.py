# Problem: 704. Binary Search
# Difficulty: EASY
# Link: https://leetcode.com/problems/binary-search/

# Pattern: Binary Search (classic)
# Approach:
# - left = 0, right = len(nums) - 1 (both valid indices)
# - while left <= right (must include when they meet)
# - mid = (left + right) // 2
# - Halve the search space each iteration

# Why O(log n):
# - Each step eliminates HALF of remaining elements
# - n → n/2 → n/4 → ... → 1
# - Takes log2(n) steps

# Time Complexity: O(log n)
# Space Complexity: O(1)

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid
        return -1

# LeetCode Result:
# Runtime: 0ms (Beats 100.00%)
# Memory: 20.57 MB (Beats 34.38%)

# Problem: 26. Remove Duplicates from Sorted Array
# Difficulty: Easy
# Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/

# Pattern: Two Pointers (In-place modification)
# Approach:
# - k pointer tracks position for next unique element
# - i pointer scans through array
# - Since array is sorted, duplicates are adjacent
# - When nums[i] != nums[i-1], place it at position k

# Time Complexity: O(n) - single pass
# Space Complexity: O(1) - in-place, no extra memory

class Solution:
    def removeDuplicates(self, nums):
        k = 1
        n = len(nums)
        for i in range(1, n):
            if nums[i] != nums[i-1]:
                nums[k] = nums[i]
                k = k + 1
        return k


# LeetCode Result:
# Runtime: 3ms (Beats 45.75%)
# Memory: 20.49 MB (Beats 78.18%)

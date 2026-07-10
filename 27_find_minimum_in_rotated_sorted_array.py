# Problem: 153. Find Minimum in Rotated Sorted Array
# Difficulty: MEDIUM
# Link: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

# Pattern: Binary Search on Rotated Array (pivot detection)
# STATUS: ❌ HINT from LeetCode on Jul 10 - MUST RE-SOLVE SOLO Jul 11

# Approach:
# - Compare nums[mid] with nums[right]
# - If nums[mid] > nums[right] → rotation point is in RIGHT half
#   → min is to the right → l = mid + 1
# - Else → min is at mid or in LEFT half
#   → r = mid  (NOT mid - 1, because mid could BE the min)
# - Loop: while l < r  (pairs with r = m to avoid infinite loop)

# KEY INSIGHT:
# Compare against nums[r] (not nums[l]) because in a rotated array,
# nums[r] is guaranteed to be <= any element in the "rotated" section.
# If nums[m] > nums[r], mid is in the "big" half, min is past it.

# Time Complexity: O(log n)
# Space Complexity: O(1)

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        return nums[l]

# LeetCode Result:
# Runtime: 0ms (Beats 100.00%)
# Memory: 19.36 MB (Beats 39.15%)

# NOTE: Approach was hinted by LeetCode. Re-solve solo Jul 11.

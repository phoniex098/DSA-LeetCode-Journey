# Problem: 33. Search in Rotated Sorted Array
# Difficulty: MEDIUM
# Link: https://leetcode.com/problems/search-in-rotated-sorted-array/

# Pattern: Binary Search on Rotated Array (identify sorted half)
# STATUS: ✅ SOLO first try. Correct but nested (2·log n).
#         Revision Jul 13 for cleaner one-pass version.

# Approach (my version — nested):
# - Outer binary search identifies which half is sorted
# - If target is in the sorted half, inner binary search finds it
# - Otherwise, narrow into the unsorted half

# Time Complexity: O(log n)  - technically 2·log n
# Space Complexity: O(1)

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] < nums[r]:
                if nums[m] <= target and nums[r] >= target:
                    while l <= r:
                        m = (l + r) // 2
                        if nums[m] > target:
                            r = m - 1
                        elif nums[m] < target:
                            l = m + 1
                        else:
                            return m
                else:
                    r = m
            else:
                if nums[m] >= target and nums[l] <= target:
                    while l <= r:
                        m = (l + r) // 2
                        if nums[m] > target:
                            r = m - 1
                        elif nums[m] < target:
                            l = m + 1
                        else:
                            return m
                else:
                    l = l + 1
        return -1

# LeetCode Result:
# Runtime: 0ms (Beats 100.00%)
# Memory: 19.40 MB (Beats 77.64%)

# CLEANER ONE-PASS VERSION (revision Jul 13):
# while l <= r:
#     m = (l+r)//2
#     if nums[m] == target: return m
#     if nums[l] <= nums[m]:              # left half sorted
#         if nums[l] <= target < nums[m]: r = m - 1
#         else: l = m + 1
#     else:                               # right half sorted
#         if nums[m] < target <= nums[r]: l = m + 1
#         else: r = m - 1
# return -1

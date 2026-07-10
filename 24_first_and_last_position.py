# Problem: 34. Find First and Last Position of Element in Sorted Array
# Difficulty: MEDIUM
# Link: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

# Pattern: Binary Search (Boundary Search — LEFT and RIGHT)
# STATUS: ❌ GOOGLED on Jul 10 - MUST RE-SOLVE SOLO Jul 11

# Approach (optimal — 2 boundary binary searches):
# - Left search: when nums[mid] == target, save mid, then push RIGHT down
# - Right search: when nums[mid] == target, save mid, then push LEFT up
# - Never do linear walk (which would make it O(k))

# Key move: DON'T RETURN when nums[mid] == target.
# Save the index, keep binary searching in one direction.

# Time Complexity: O(log n)  - two independent binary searches
# Space Complexity: O(1)

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def find_bound(is_left: bool) -> int:
            left, right = 0, len(nums) - 1
            bound = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] > target:
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    bound = mid
                    if is_left:
                        right = mid - 1
                    else:
                        left = mid + 1
            return bound
        return [find_bound(True), find_bound(False)]

# LeetCode Result:
# Runtime: 0ms (Beats 100.00%)
# Memory: 20.53 MB (Beats 59.39%)

# NOTE: This code was GOOGLED. Concept understood after explanation,
#       but hands-on solo re-solve pending Jul 11.

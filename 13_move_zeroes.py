# Problem: 283. Move Zeroes
# Difficulty: Easy
# Link: https://leetcode.com/problems/move-zeroes/

# Pattern: Two Pointers (Fast/Slow)
# Approach:
# - Slow pointer (k): position to place next non-zero
# - Fast pointer (i): scans through array
# - When non-zero found, swap with position k, then k++

# Time Complexity: O(n) - single pass
# Space Complexity: O(1) - in-place swaps

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        k = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[k] = nums[k], nums[i]
                k = k + 1


# ═══════════════════════════════════════════
# FAILED ATTEMPT (Learning Record)
# ═══════════════════════════════════════════
# ❌ First attempt: O(n²) with nested loops and slicing
# Runtime: 4610ms (Beats 5%)
# Lesson: When you see "in-place" + "move X" → THINK TWO POINTERS FIRST


# LeetCode Result (Correct):
# Runtime: 4ms (Beats 60.14%)
# Memory: 20.63 MB (Beats 23.52%)

# Problem: 1. Two Sum
# Difficulty: Easy
# Pattern: HashMap Complement Search

# ❌ Approach 1: Brute Force (Nested Loops)
# Time: O(n²) | Space: O(1)
# Runtime: 1755ms (Beats 13%)
class SolutionBrute:
    def twoSum(self, nums, target):
        n = len(nums)
        for i in range(n):
            for p in range(i+1, n):
                if nums[p] + nums[i] == target:
                    return [i, p]

# ✅ Approach 2: HashMap (Optimal)
# Time: O(n) | Space: O(n)
# Runtime: 0ms (Beats 100%)
class Solution:
    def twoSum(self, nums, target):
        s = {}
        for i, n in enumerate(nums):
            j = target - n
            if j in s:
                return [s[j], i]
            s[n] = i

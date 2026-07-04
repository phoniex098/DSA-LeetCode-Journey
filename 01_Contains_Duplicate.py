# Problem: 217. Contains Duplicate
# Difficulty: Easy
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def containsDuplicate(self, nums):
        return len(nums) != len(set(nums))

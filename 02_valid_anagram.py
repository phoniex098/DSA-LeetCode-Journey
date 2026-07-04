# Problem: 242. Valid Anagram
# Difficulty: Easy
# Pattern: Sorting comparison
# Time Complexity: O(n log n)
# Space Complexity: O(1)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

# Problem: 3. Longest Substring Without Repeating Characters
# Difficulty: MEDIUM
# Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/

# Pattern: Sliding Window (Variable Size)
# Approach:
# - Expand window by moving right pointer
# - Track each char's LAST SEEN INDEX in a HashMap
# - When we hit a duplicate that is INSIDE the window,
#   jump left to (last_seen_index + 1)
# - Update max length every iteration

# Why max(left, dic[char] + 1):
# - The duplicate's stored index might be BEHIND current left
#   (a stale entry from before the window shrank)
# - max() ensures left never moves backward

# Time Complexity: O(n) - right traverses once, left never goes back
# Space Complexity: O(min(n, k)) - k = char set size (26/128)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        m = 0
        dic = {}
        for right in range(len(s)):
            if s[right] in dic:
                left = max(left, dic[s[right]] + 1)
            dic[s[right]] = right
            m = max(m, right - left + 1)
        return m

# LeetCode Result:
# Runtime: 13ms (Beats 50.26%)
# Memory: 19.12 MB (Beats 92.48%)

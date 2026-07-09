# Problem: 76. Minimum Window Substring
# Difficulty: HARD
# Link: https://leetcode.com/problems/minimum-window-substring/

# Pattern: Sliding Window (Variable Size) + have/need counter
# Approach:
# - Build dic1 = freq of t (what we NEED)
# - Slide window over s, maintain dic2 = freq of current window
# - Track `have` = number of unique chars satisfied (dic2[c] >= dic1[c])
# - Window is VALID when have == need
# - For MIN problems: shrink WHILE valid (find smallest still-valid)
# - For MAX problems: shrink WHILE invalid (see #424)

# Time Complexity: O(n + k) where n=len(s), k=len(t)
# Space Complexity: O(k) for the freq dicts

# TO REVISE: Jul 13 (needed hint on min-shrink direction & have/need trick)

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m = len(s)
        n = len(t)
        if n > m:
            return ""
        se = set(t)
        l = r = left = 0
        h = float("inf")
        have = 0
        dic1 = {}
        dic2 = {}
        for i in range(n):
            dic1[t[i]] = dic1.get(t[i], 0) + 1
        need = len(dic1)
        for right in range(m):
            if s[right] in se:
                dic2[s[right]] = dic2.get(s[right], 0) + 1
                if dic2[s[right]] == dic1[s[right]]:
                    have += 1
            while need == have:
                if right - left + 1 < h:
                    h = right - left + 1
                    r = right
                    l = left
                if s[left] in se:
                    dic2[s[left]] -= 1
                    if dic2[s[left]] < dic1[s[left]]:
                        have -= 1
                left += 1
        if h == float("inf"):
            return ""
        return s[l:r+1]

# LeetCode Result:
# Runtime: 68ms (Beats 56.63%)  [Optimized from 677ms with have/need trick]
# Memory: 19.83 MB (Beats 11.67%)

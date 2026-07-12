# Problem: 424. Longest Repeating Character Replacement
# Difficulty: MEDIUM
# Link: https://leetcode.com/problems/longest-repeating-character-replacement/

# Pattern: Sliding Window (Variable Size)
# Approach:
# - Expand window by moving right, track char frequencies in HashMap
# - Track m = max frequency ever seen in any window
# - Window is VALID when: (window_length - m) <= k
#   (means we can replace <= k chars to make all same)
# - While window is INVALID, shrink from left
# - Record max window length every iteration

# Why we DON'T decrement m when shrinking:
# - We want ans to be the MAXIMUM valid window length
# - For ans to grow past current best, we need m >= ans - k
# - m only grows past best-so-far freq, so this stays true
# - A stale (too-high) m may let invalid windows pass the check,
#   but those windows are shorter than ans → never affect answer

# Rule of thumb:
# - Answer = MAX over history → stale/overestimated state is OK
# - Answer = CURRENT value    → state must be exact

# Time Complexity: O(n) - right and left each traverse once
# Space Complexity: O(k) - k = distinct chars (<= 26 for uppercase)

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        dic = {}
        m = 0
        ans = 0
        for right in range(len(s)):
            # EXPAND
            dic[s[right]] = dic.get(s[right], 0) + 1
            m = max(m, dic[s[right]])
            # SHRINK while invalid
            while (right - left + 1) - m > k:
                dic[s[left]] -= 1
                left += 1
            # RECORD
            ans = max(ans, right - left + 1)
        return ans

# LeetCode Result:
# Runtime: 81ms (Beats 62.92%)
# Memory: 19.70 MB (Beats 49.90%)

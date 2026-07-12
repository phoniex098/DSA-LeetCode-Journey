# Problem: 567. Permutation in String
# Difficulty: MEDIUM
# Link: https://leetcode.com/problems/permutation-in-string/

# Pattern: Sliding Window (Fixed Size) + Frequency Comparison
# Approach:
# - Build freq dict of s1 (dic1)
# - Slide a window of size len(s1) across s2, maintain dic2
# - Compare dic1 == dic2 at each valid window
# - When shrinking, delete key entirely if count hits 0
#   (otherwise stale zero-entries break dict equality)

# Time Complexity: O(n + k) where n=len(s1), k=len(s2)
# Space Complexity: O(1) - at most 26 keys

# TO REVISE: Jul 12 (got hint from AI on the two-dict approach)

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        k = len(s2)
        if n > k:
            return False
        dic1 = {}
        dic2 = {}
        for i in range(n):
            dic1[s1[i]] = dic1.get(s1[i], 0) + 1
        left = 0
        for right in range(k):
            dic2[s2[right]] = dic2.get(s2[right], 0) + 1
            if right - left + 1 == n:
                if dic1 == dic2:
                    return True
                key = s2[left]
                if dic2[key] == 1:
                    del dic2[key]
                else:
                    dic2[key] -= 1
                left += 1
        return False

# LeetCode Result:
# Runtime: 15ms (Beats 81.15%)
# Memory: 19.40 MB (Beats 52.97%)

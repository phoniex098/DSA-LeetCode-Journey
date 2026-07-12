# Problem: 49. Group Anagrams
# Difficulty: MEDIUM
# Link: https://leetcode.com/problems/group-anagrams/

# Pattern: HashMap with Sorted String as Key
# Approach:
# - All anagrams produce same string when sorted
# - Use sorted string as HashMap key
# - Group original strings under their sorted signature

# Time Complexity: O(n * k log k)
#   where n = number of strings, k = max string length
# Space Complexity: O(n * k) - storing all strings in dict

class Solution:
    def groupAnagrams(self, strs):
        d = {}
        for n in strs:
            s = "".join(sorted(n))
            if s in d:
                d[s].append(n)
            else:
                d[s] = []
                d[s].append(n)
        return list(d.values())


# LeetCode Result:
# Runtime: 15ms (Beats 42.32%)
# Memory: 21.83 MB (Beats 87.89%)

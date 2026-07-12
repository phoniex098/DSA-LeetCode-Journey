# Problem: 125. Valid Palindrome
# Difficulty: Easy

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        t = []
        for l in s:
            if l.isalnum():
                t.append(l)
        n = len(t)
        i = 0
        j = n - 1
        while i < j:
            if t[i] != t[j]:
                return False
            i += 1
            j -= 1
        return True

# Problem: 100. Same Tree
# Difficulty: EASY
# Link: https://leetcode.com/problems/same-tree/

# Pattern: Tree Recursion — walk TWO trees in lockstep
# Approach:
# - Base case: if either is None, they're same iff both are None
#   → return p == q  (True if both None, False if only one None)
# - Recurse: same values AND same left subtrees AND same right subtrees

# BUG I HAD:
# First attempt: recursed on children but forgot to compare p.val == q.val.
# Result: any two trees with same shape returned True regardless of values.
# FIX: always compare current values BEFORE trusting children.

# Time Complexity: O(min(n, m))  - stops at first mismatch or shorter tree
# Space Complexity: O(min(h_p, h_q))

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None or q is None:
            return p == q
        return (p.val == q.val 
                and self.isSameTree(p.right, q.right) 
                and self.isSameTree(p.left, q.left))

# LeetCode Result:
# Runtime: 0ms (Beats 100.00%)
# Memory: 19.37 MB (Beats 30.28%)

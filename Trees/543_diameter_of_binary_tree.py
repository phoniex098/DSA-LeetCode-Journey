# Problem: 543. Diameter of Binary Tree
# Difficulty: EASY (misleading — really Medium in disguise)
# Link: https://leetcode.com/problems/diameter-of-binary-tree/

# Pattern: Tree Recursion + Sidechannel Tracking (self.n)
# Approach:
# - Diameter can pass through ANY node, not just root
# - At each node: path passing through = left_depth + right_depth
# - Do a single-pass DFS that computes depth AND records max diameter

# KEY LESSONS LEARNED:
# 1. First attempt only checked diameter through root — wrong.
#    Diameter can occur at ANY node in the tree.
# 2. Called self.maxi(left)/self.maxi(right) FOUR times per node
#    → exponential O(4^n). CACHE recursive calls into local vars.

# SIDECHANNEL TRICK:
# When you need to return one thing (depth) AND track another
# thing globally (max diameter), use self.n as sidechannel.

# Time Complexity: O(n)   - each node visited exactly once
# Space Complexity: O(h)  - recursion stack

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.n = 0
        self.maxi(root)
        return self.n

    def maxi(self, root):
        if root is None:
            return 0
        l = self.maxi(root.left)
        r = self.maxi(root.right)
        self.n = max(l + r, self.n)
        return 1 + max(l, r)

# LeetCode Result:
# Runtime: 0ms (Beats 100.00%)
# Memory: 21.99 MB (Beats 98.06%)

# CRITICAL RULE (from bug):
# BAD:  self.n = max(self.maxi(root.left) + self.maxi(root.right), self.n)
#       return 1 + max(self.maxi(root.left), self.maxi(root.right))
#       → 4 recursive calls per node → O(4^n) exponential
#
# GOOD: l = self.maxi(root.left)
#       r = self.maxi(root.right)
#       self.n = max(l + r, self.n)
#       return 1 + max(l, r)
#       → 2 calls per node, reuse → O(n) linear

# Problem: 110. Balanced Binary Tree
# Difficulty: EASY
# Link: https://leetcode.com/problems/balanced-binary-tree/

# Pattern: Tree Recursion + Sidechannel Tracking (self.n)
# Approach (V1 — SUBMITTED, naive O(n²)):
# - At each node, compute heights of both subtrees using maxi()
# - If diff > 1, return False
# - Recurse into both subtrees
# - Redundant work: maxi() gets called at every level

# OPTIMAL APPROACH (V2 — sidechannel, O(n)):
# - Same sidechannel trick as #543
# - Single DFS computes height at each node
# - If any node has imbalance, flip self.n to False
# - Total work: O(n) vs O(n²) for V1

# Balanced = for EVERY node: |left_height - right_height| ≤ 1

# Time Complexity (V1 submitted): O(n²) worst case
# Time Complexity (V2 optimal):   O(n)
# Space Complexity: O(h)

# V1 (submitted — naive but works)
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        l = self.maxi(root.right)
        r = self.maxi(root.left)
        if abs(l - r) > 1:
            return False
        return self.isBalanced(root.right) and self.isBalanced(root.left)

    def maxi(self, root):
        if root is None:
            return 0
        l = self.maxi(root.left)
        r = self.maxi(root.right)
        return 1 + max(l, r)

# LeetCode Result (V1):
# Runtime: 6ms (Beats 20.51%)
# Memory: 20.33 MB (Beats 70.23%)

# V2 (OPTIMAL — sidechannel, for reference)
# class Solution:
#     def isBalanced(self, root):
#         self.n = True
#         self.maxi(root)
#         return self.n
#
#     def maxi(self, root):
#         if root is None: return 0
#         l = self.maxi(root.left)
#         r = self.maxi(root.right)
#         if abs(l - r) > 1: self.n = False
#         return 1 + max(l, r)

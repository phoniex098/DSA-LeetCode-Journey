# Problem: 235. Lowest Common Ancestor of a Binary Search Tree
# Difficulty: MEDIUM
# Link: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

# Pattern: BST / Binary Search on Tree
# Approach:
# - Exploit BST property: left subtree < root < right subtree
# - If both p and q are LESS than root → LCA is in left subtree
# - If both are GREATER than root → LCA is in right subtree
# - Otherwise (split or one equals root) → root IS the LCA

# Key Insight:
# - This IS binary search, on a tree instead of an array
# - Each comparison eliminates half the tree → O(h)

# Time Complexity: O(h) — balanced O(log n), skewed O(n)
# Space Complexity: O(h) recursion stack

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        elif root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return root

# LeetCode Result:
# Runtime: 71ms (Beats 22%)
# Memory: 22.69 MB (Beats 67%)
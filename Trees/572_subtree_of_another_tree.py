# Problem: 572. Subtree of Another Tree
# Difficulty: EASY (misleading — really Medium in disguise)
# Link: https://leetcode.com/problems/subtree-of-another-tree/

# Pattern: Two-layer Tree Recursion
# STATUS: ❌ GOOGLED on Jul 11 - MUST RE-SOLVE SOLO Jul 12 (blank editor)

# Approach (two nested recursions):
# - Outer isSubtree: walks every node of `root`
# - At each node, calls isSameTree(node, subRoot) - reuses #100 logic
# - If any node matches, return True
# - If root is None, subRoot cannot be found → return False

# KEY INSIGHT:
# When a problem needs "check property X at every node", combine
# a TRAVERSAL recursion (outer) with a CHECK recursion (inner).
# Reuse solved subproblems - don't re-derive isSameTree here.

# Time Complexity: O(n·m)  - for each node in root, may check whole subRoot
# Space Complexity: O(h_root + h_subRoot)

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None:
            return False
        if self.istree(root, subRoot):
            return True
        return self.isSubtree(root.right, subRoot) or self.isSubtree(root.left, subRoot)

    def istree(self, root, subRoot):
        if root is None or subRoot is None:
            return root == subRoot
        return (root.val == subRoot.val
                and self.istree(root.right, subRoot.right)
                and self.istree(root.left, subRoot.left))

# LeetCode Result:
# Runtime: 19ms (Beats 92.75%)
# Memory: 19.46 MB (Beats 85.69%)

# NOTE: Code was GOOGLED. Concept understood after seeing solution,
#       but hands-on solo re-solve pending Jul 12.

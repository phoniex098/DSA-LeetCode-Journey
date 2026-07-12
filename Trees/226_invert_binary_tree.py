# Problem: 226. Invert Binary Tree
# Difficulty: EASY
# Link: https://leetcode.com/problems/invert-binary-tree/

# Pattern: Tree Recursion (universal template)
# Approach:
# - Base case: if node is None, return None
# - Swap left and right children (Python tuple swap)
# - Recurse into both children
# - Return root

# Universal recursive template applied:
#   solve(node):
#     if node is None: return <base>
#     left  = solve(node.left)
#     right = solve(node.right)
#     return <combine>
# Here combine = swap + return root

# Time Complexity: O(n)   - visit every node once
# Space Complexity: O(h)  - recursion stack (h = tree height)

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        root.left, root.right = root.right, root.left
        self.invertTree(root.right)
        self.invertTree(root.left)
        return root

# LeetCode Result:
# Runtime: 0ms (Beats 100.00%)
# Memory: 19.22 MB (Beats 59.83%)

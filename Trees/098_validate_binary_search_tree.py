# Problem: 98. Validate Binary Search Tree
# Difficulty: MEDIUM
# Link: https://leetcode.com/problems/validate-binary-search-tree/

# Pattern: Bounded Recursion (Tree)
# Approach:
# - Every node has a valid RANGE (low, high) it must fall within
# - Root starts with (-inf, +inf)
# - Recursing LEFT: new range = (low, node.val)
# - Recursing RIGHT: new range = (node.val, high)
# - Fail immediately if node.val is outside its bounds

# Key Insight:
# - Naive left.val < root < right.val is WRONG — must check against ALL ancestors
# - Bounds propagate downward, tightening as we recurse
# - STRICT inequality because BST forbids duplicates

# Time Complexity: O(n)
# Space Complexity: O(h)

class Solution:
    def isValidBST(self, root):
        def validate(node, low, high):
            if not node:
                return True
            if node.val <= low or node.val >= high:
                return False
            return (validate(node.right, node.val, high) and
                    validate(node.left, low, node.val))
        return validate(root, float('-inf'), float('inf'))

# LeetCode Result:
# Runtime: 0ms (Beats 100%)
# Memory: 20.94 MB (Beats 45%)
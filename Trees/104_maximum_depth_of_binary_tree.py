# Problem: 104. Maximum Depth of Binary Tree
# Difficulty: EASY
# Link: https://leetcode.com/problems/maximum-depth-of-binary-tree/

# Pattern: Tree Recursion — return depth UP the call stack
# Approach:
# - Base case: empty tree has depth 0
# - Recurse: get depth of left and right subtrees
# - Combine: current depth = 1 + max(left_depth, right_depth)

# LESSON LEARNED:
# First attempt used accumulator (pushing depth DOWN as parameter).
# Broken because I threw away return values of recursive calls.
# CORRECT STYLE: return depth UP from base case.
# For most tree problems, "return up" beats "push down".

# Time Complexity: O(n)
# Space Complexity: O(h)

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return 1 + max(self.maxDepth(root.right), self.maxDepth(root.left))

# LeetCode Result:
# Runtime: 0ms (Beats 100.00%)
# Memory: 22.57 MB (Beats 6.65%)

# Problem: 199. Binary Tree Right Side View
# Difficulty: MEDIUM
# Link: https://leetcode.com/problems/binary-tree-right-side-view/

# Pattern: BFS (Breadth-First Search)
# Approach:
# - Standard BFS level order
# - At each level, capture only the LAST node's value (rightmost)
# - Use `if i == l - 1` inside the level loop to detect last node

# Key Insight:
# - Right side view = last node of each level in BFS order
# - Don't use q[-1] before/after loop — fragile, passes by coincidence
# - Detect last node inline: cleaner, single-pass, explainable

# Time Complexity: O(n)
# Space Complexity: O(n)

from collections import deque

class Solution:
    def rightSideView(self, root):
        if not root:
            return []
        q = deque([root])
        ans = []
        while q:
            l = len(q)
            for i in range(l):
                node = q.popleft()
                if i == l - 1:
                    ans.append(node.val)
                if node.left:  q.append(node.left)
                if node.right: q.append(node.right)
        return ans

# LeetCode Result:
# Runtime: 0ms (Beats 100%)
# Memory: 19.22 MB (Beats 69%)
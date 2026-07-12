# Problem: 102. Binary Tree Level Order Traversal
# Difficulty: MEDIUM
# Link: https://leetcode.com/problems/binary-tree-level-order-traversal/

# Pattern: BFS (Breadth-First Search)
# Approach:
# - Use deque as FIFO queue
# - Snapshot level size with len(q) BEFORE processing children
# - Process exactly that many nodes → those form one level
# - Append their children for next iteration

# Key Insight:
# - len(q) captured at start of each while iteration = current level width
# - Guard appends with `if node.left` to keep None out of queue
# - Use collections.deque, NOT list — popleft is O(1) vs list.pop(0) O(n)

# Time Complexity: O(n) — every node visited once
# Space Complexity: O(n) — queue holds widest level

from collections import deque

class Solution:
    def levelOrder(self, root):
        if not root:
            return []
        q = deque([root])
        ans = []
        while q:
            l = len(q)
            level = []
            for _ in range(l):
                node = q.popleft()
                level.append(node.val)
                if node.left:  q.append(node.left)
                if node.right: q.append(node.right)
            ans.append(level)
        return ans

# LeetCode Result:
# Runtime: 0ms (Beats 100%)
# Memory: 20.05 MB (Beats 24%)
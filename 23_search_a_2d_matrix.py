# Problem: 74. Search a 2D Matrix
# Difficulty: MEDIUM
# Link: https://leetcode.com/problems/search-a-2d-matrix/

# Pattern: Binary Search (row-scan + col binary search)
# NOTE: This is SUBOPTIMAL (O(n log m)).
#       Optimal is O(log(n·m)) by treating matrix as flat 1D sorted array.
#       Re-solve with flat approach: revision Jul 12.

# Approach used (suboptimal):
# - Scan each row: if target is between row[0] and row[-1], binary search that row
# - Also handles edge cases where target equals first/last of a row

# Time Complexity: O(n log m)   [suboptimal - should be O(log(n·m))]
# Space Complexity: O(1)

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0]) - 1
        left = 0
        right = m
        for i in range(n):
            if matrix[i][0] < target and matrix[i][m] > target:
                while left <= right:
                    mid = (left + right) // 2
                    if matrix[i][mid] > target:
                        right = mid - 1
                    elif matrix[i][mid] < target:
                        left = mid + 1
                    else:
                        return True
            elif matrix[i][0] == target or matrix[i][m] == target:
                return True
        return False

# LeetCode Result:
# Runtime: 0ms (Beats 100.00%)
# Memory: 19.38 MB (Beats 96.71%)

# OPTIMAL APPROACH (for revision Jul 12):
# - Flat index: 0 to n*m - 1
# - row = i // cols, col = i % cols
# - Single binary search over n*m elements
# - O(log(n·m)) time

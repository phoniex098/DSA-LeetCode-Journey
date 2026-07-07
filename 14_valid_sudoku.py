# Problem: 36. Valid Sudoku
# Difficulty: MEDIUM
# Link: https://leetcode.com/problems/valid-sudoku/

# Pattern: HashSet with Multiple Sets in Parallel
# Approach:
# - 3 lists of sets: rows[9], cols[9], boxes[9]
# - Single pass through 81 cells
# - For each cell, check all 3 sets simultaneously
# - Formula for box_id: (i//3) * 3 + (j//3)

# Time Complexity: O(1) - fixed 9x9 board
# Space Complexity: O(1) - fixed size sets

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        box = [set() for _ in range(9)]
        
        for i in range(9):
            for j in range(9):
                b = (i // 3) * 3 + (j // 3)
                k = board[i][j]
                if k == '.':
                    continue
                if k in row[i] or k in col[j] or k in box[b]:
                    return False
                row[i].add(k)
                col[j].add(k)
                box[b].add(k)
        return True


# ═══════════════════════════════════════════
# FAILED ATTEMPT (Learning Record)
# ═══════════════════════════════════════════
# ❌ First attempt: 97 lines with 11 copy-pasted blocks (one per box)
# Lesson: When you see repetition in your code, FIND THE FORMULA
# The formula (i//3)*3 + (j//3) maps 2D → 1D for boxes


# LeetCode Result:
# Runtime: 4ms (Beats 47.67%)
# Memory: 19.37 MB (Beats 34.16%)

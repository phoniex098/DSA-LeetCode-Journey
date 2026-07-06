# Problem: 238. Product of Array Except Self
# Difficulty: MEDIUM
# Link: https://leetcode.com/problems/product-of-array-except-self/

# Pattern: Prefix & Suffix Products (Two Pass)
# Note: Watched NeetCode video for approach
# Need to re-solve on July 8 without help to confirm learning

# Constraints:
# - No division allowed
# - Must run in O(n) time
# - Ideally O(1) extra space (output array doesn't count)

# Approach:
# 1. First pass (left to right): Build product of all elements to the LEFT
# 2. Second pass (right to left): Multiply by product of all elements to the RIGHT
# 3. Result: answer[i] = product of everything except nums[i]

# Time Complexity: O(n) - two linear passes
# Space Complexity: O(1) - only pre and post variables (output not counted)

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = []
        answer.append(1)              # position 0 has no left elements
        answer.append(nums[0])         # position 1: left is just nums[0]
        pre = nums[0]
        post = 1
        
        # First pass: Build left products
        for i in range(2, n):
            answer.append(nums[i-1] * pre)
            pre = answer[i]
        
        # Second pass: Multiply by right products
        for i in range(n-1, -1, -1):
            answer[i] = answer[i] * post
            post = post * nums[i]
        
        return answer


# ═══════════════════════════════════════════
# FAILED ATTEMPTS (Learning Record)
# ═══════════════════════════════════════════

# ❌ Attempt 1: Used division (//) - VIOLATED CONSTRAINT
# Would fail in real interview even though LeetCode accepted it
#
# class Solution:
#     def productExceptSelf(self, nums):
#         prod = 1
#         k = 0
#         for n in nums:
#             if n != 0:
#                 prod = prod * n
#             else:
#                 k = k + 1
#         answer = []
#         for n in nums:
#             if n != 0 and k == 0:
#                 answer.append(prod // n)   # ⚠️ DIVISION - not allowed
#             ...


# ❌ Attempt 2: Used math.prod() - O(n²) time, still cheating
# Violated the O(n) time constraint
#
# class Solution:
#     def productExceptSelf(self, nums):
#         answer = []
#         n = len(nums)
#         for i in range(n):
#             prod = math.prod(nums[:i]) * math.prod(nums[i+1:])   # O(n) inside loop
#             answer.append(prod)                                    # Total: O(n²)
#         return answer


# ═══════════════════════════════════════════
# LESSON LEARNED
# ═══════════════════════════════════════════
# When a problem has explicit constraints, RESPECT them.
# "No division" and "O(n) time" exist to test a specific pattern.
# Bypassing constraints = failing the interview.
# Learn the intended pattern (prefix/suffix products here).


# LeetCode Result (Attempt 3 - Correct):
# Runtime: 22ms (Beats 58.29%)
# Memory: 25.48 MB (Beats 70.43%)

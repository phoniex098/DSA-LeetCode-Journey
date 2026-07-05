# Problem: 20. Valid Parentheses
# Difficulty: Easy

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for l in s:
            if l == '(' or l == '{' or l == '[':
                stack.append(l)
            elif l == ')':
                if not stack or stack[-1] != '(':
                    return False
                stack.pop()
            elif l == '}':
                if not stack or stack[-1] != '{':
                    return False
                stack.pop()
            elif l == ']':
                if not stack or stack[-1] != '[':
                    return False
                stack.pop()
        return len(stack) == 0

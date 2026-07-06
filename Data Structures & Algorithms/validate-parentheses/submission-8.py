class Solution:
    def isValid(self, s: str) -> bool:

        brackets = {')': '(', '}': '{', ']': '['}
        stack = []
        opens = "( { ["


        for b in s:
            if b in brackets:
                if stack and stack[-1] == brackets[b]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(b)
                
        if not stack:
            return True
        else:
            return False


        
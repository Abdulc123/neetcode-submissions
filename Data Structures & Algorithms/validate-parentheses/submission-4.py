class Solution:
    def isValid(self, s: str) -> bool:
        
        # every open bracke ( is clsoed with the same matching bracket )
        # open brackets are closed in the correct order
        # every closing bracket should have an open bracket that is the same time

        stack = []
        brackets = {')': '(', '}': '{' , ']': '['}

        for b in s:
            
            # check if it is a closed bracket
            if b in brackets:
                if stack and stack[-1] == brackets[b]: # if stack has values
                    stack.pop()
                else: # has no values in the stack and a closed bracket was seen meaning it is not valid
                    return False
            else: # we know it is an open bracket
                stack.append(b)
            

        # we can only return true if the stack is fully empty, meaning all the pairs have been found
        if not stack:
            return True
        else:
            return False



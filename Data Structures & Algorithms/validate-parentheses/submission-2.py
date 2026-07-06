class Solution:
    def isValid(self, s: str) -> bool:
        
        # use a stack
        stack = []

        # Create a dictionary to store the open and closed bracket pairs
        formatDict = {')': '(', '}':'{', ']':'['}
        n = len(s)
        # Iterate through all the brackets in the string
        for bracket in s:
            # if a closed bracket is seen, check the top of the stack (if not empty) and make sure it matches the open bracket
            if bracket in formatDict:
                if stack and stack[-1] == formatDict[bracket]: # if the stack is not empty
                    stack.pop()
                else:
                    return False
                
            # if an open bracket is seen add it to the stack
            else:
                stack.append(bracket)
            

        # else return True only if the not(stack is not empty) = stack is empty
        if not stack:
            return True
        else:
            return False

            



class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #Rules:
        #1. Open can be added while open < n
        #2. Closed can be added when closed < open
        #3. Valid when open == closed == n

        stack = []
        result = []

        def backtrack(openN, closedN):
            if openN == closedN == n:
                result.append("".join(stack))
            
            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop()

            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()

        backtrack(0,0)   
        return result     
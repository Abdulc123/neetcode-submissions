class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # stack [1,2]
        # + 
        # [3]
        # [3,3]
        # *
        # [9]
        # [9,4]
        # -
        # [5] = result

        # anytime an operator is not seen add it to the stack
        
        # if operand is seen, figure out what to do with it, pop the two values from stack and replace with result

        # final answer will be what remains in the top of the stack

        ops = "+ - * /"
        stack = []

        for val in tokens:
            print(stack)
            if val not in ops: # we know its an integer so append to the stack
                stack.append(int(val))
            
            elif val in ops: # we know an operator is encountered
                second = stack.pop()
                first = stack.pop()

                if val == "+":
                    result = first + second
                elif val == "-":
                    result = first - second
                elif val ==  "*":
                    result = first * second
                elif val == "/":
                    result = int(first / second)
                
                stack.append(result)
        
        return stack[-1]



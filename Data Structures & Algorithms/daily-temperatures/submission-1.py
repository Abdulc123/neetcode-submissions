class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        

        # add element to stack
        # if new element is greater than top of stack, (while loop until new value is not greater than elements in stack)
        #   add the r - i value for the count
        #   pop from the stack and add the new value
        #   

        # [_30,38,30,36,35,40,28] stack = [30] result = []
        # [30,_38,30,36,35,40,28] stack = [38] result = [1,] 1 - 0
        # [30,38,_30,36,35,40,28] stack = [38, 30] result = [1,]
        # [30,38,30,_36,35,40,28] stack = [38, 30, 36] result = [1,]
        # [30,38,30,36,_35,40,28] stack = [38, 30, 36, 35] result = [1,]
        # [30,38,30,36,35,_40,28] stack = [40, ] result = [1,4,1,2,1,0,0]
        # [30,38,30,36,35,40,_28] stack = [40, 28] result = [1,4,1,2,1,0,0]

        n = len(temperatures)
        result = [0] * n

        stack = []
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                # Get the val, and index from the stack key val pair
                stackVal, stackIndex =  stack.pop()
                result[stackIndex] = i - stackIndex # Calculate the count difference between the two 
            # now add the new value on top of the stack, when its not greater than any more values
            stack.append([t, i])

        return result


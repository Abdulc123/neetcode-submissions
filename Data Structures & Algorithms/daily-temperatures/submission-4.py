class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # return a list of days for each temp[i] where the number of days
        # represents how many days until a warmer temp appeared 
        # future temp > ith day temp

        # keep track of index, temp in stack
        # remove from top of stack while the current element is greater than
        # take the difference of the index

        n = len(temperatures)
        stack = []
        result = [0] * n

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                prev_i = stack[-1][1]
                result[prev_i] = i - prev_i
                stack.pop()
            
            stack.append([temp, i])
        
        return result


            


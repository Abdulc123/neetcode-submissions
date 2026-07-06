class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        # add the temperature to the stack
        # if the stack has elements in it, check what is on the top and if it is warmer you know it was one check

        
        n = len(temperatures)
        result = [0] * n
        stack = []

        # [(30, 0)] result = [1,0,0,0,0,0,0]
        # [(38, 1), (30,2) (36,3)] = result = [1,0,1,0,0,0,0]

        for i, temp in enumerate(temperatures):

            while stack and temp > stack[-1][0]:
                oldTemp, oldIndex = stack[-1]
                result[oldIndex] = i - oldIndex
                stack.pop()


            stack.append((temp, i))


        return result


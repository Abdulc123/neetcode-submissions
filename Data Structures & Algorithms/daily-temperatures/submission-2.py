class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        # add the temperature to the stack
        # if the stack has elements in it, check what is on the top and if it is warmer you know it was one check

        
        n = len(temperatures)
        result = [0] * n
        for i in range(n):
            for j in range(i + 1, n):
                if temperatures[j] > temperatures[i]:
                    result[i] = j - i
                    break
        




        
        return result


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        n = len(temperatures)
        result = []

        for i in range(n):
            j = i + 1
            while j < n:
                if temperatures[j] > temperatures[i]:
                    result.append(j - i)
                    break

                j += 1
            if j == n: #no match was found
                result.append(0)
            
        return result



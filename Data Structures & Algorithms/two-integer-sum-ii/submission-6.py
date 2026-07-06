class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        # array is filled with integers
        # is in increasing order, always a valid solution, must be done using O(1) space

        # return indexes of two numbers in a list that add up to target i1 + i2 = target
        # index1 < index2
        # index1 != index2

        # 1 2 3 4 target = 6
        # 12 13 14
        # 23 24 target = 2,4

        # Two pointer Approach

        i = 0
        j = len(numbers) - 1

        while i < j:
            current = numbers[i] + numbers[j]
            # we want to find i1 and i2 that equal target
            if current < target:
                i += 1
            elif current > target:
                j -=1
            else: # they equal one another
                return [i + 1, j + 1]






        # result = []
        # i = 0
        # n = len(numbers)

        # while i < n :
        #     j = i + 1

        #     while j < n:
        #         print(numbers[i], numbers[j], i, j)
        #         if numbers[i] + numbers[j] == target:
        #             return [i + 1, j + 1]
                
        #         j += 1
            
        #     # if no match was found move i up by 1
        #     i += 1



        # # Brute force using dictionary tracking the index of each number
        # indexDict = {}
        # n = len(numbers)
        # # Creating the value : index dict
        # for i in range(n):
        #     indexDict[numbers[i]] = i
        #     print(indexDict)

        #     # Look for the value
        #     diff = target - numbers[i]
            
        #     if diff in indexDict and indexDict[diff] != i: 
        #         return [indexDict[diff] + 1, i + 1]
        
    
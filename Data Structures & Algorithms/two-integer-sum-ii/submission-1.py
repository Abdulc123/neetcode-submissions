class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        # array is filled with integers
        # is in increasing order, always a valid solution, must be done using O(1) space

        # return indexes of two numbers in a list that add up to target i1 + i2 = target
        # index1 < index2
        # index1 != index2

        result = []

        # Brute force using dictionary tracking the index of each number
        indexDict = {}
        n = len(numbers)
        # Creating the value : index dict
        for i in range(n):
            indexDict[numbers[i]] = i
            print(indexDict)

            # Look for the value
            diff = target - numbers[i]
            
            if diff in indexDict and indexDict[diff] != i: 
                return [indexDict[diff] + 1, i + 1]
        
    